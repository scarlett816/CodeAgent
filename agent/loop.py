from rich.console import Console

from prompts.system_prompt import SYSTEM_PROMPT
from agent.parser import Parser
from agent.executor import Executor
from agent.memory import Memory


console = Console()


class AgentLoop:

    def __init__(self, llm):

        self.llm = llm

        self.parser = Parser()

        self.executor = Executor()

        self.memory = Memory()

    def run(self, user_input: str):

        self.memory.add_user(user_input)

        MAX_STEP = 10

        final_answer = ""

        for step in range(MAX_STEP):

            console.print()

            console.rule(f"[yellow]Step {step + 1}")

            #
            # 构造 messages
            #

            messages = [

                {

                    "role": "system",

                    "content": SYSTEM_PROMPT

                }

            ]

            messages.extend(

                self.memory.get_messages()

            )

            #
            # 调用模型
            #

            try:

                response = self.llm.chat(messages)

            except Exception as e:

                console.print(f"[red]{e}[/red]")

                return str(e)

            console.print()

            console.print("[cyan]LLM 输出：[/cyan]")

            console.print(response)

            #
            # 保存 assistant 原始输出
            #

            self.memory.add_assistant(response)

            #
            # JSON 解析
            #

            action = self.parser.parse(response)

            if action is None:

                console.print()

                console.print("[red]JSON 解析失败[/red]")

                self.memory.add_tool(

                    "JSON解析失败，请重新输出合法JSON。"

                )

                continue

            #
            # FINAL
            #

            if action.get("action") == "final":

                final_answer = action.get(

                    "answer",

                    ""

                )

                console.print()

                console.print("[green]任务完成[/green]")

                return final_answer

            #
            # Tool
            #

            result = self.executor.execute(action)

            console.print()

            console.print("[green]工具执行结果：[/green]")

            #
            # read_file 特殊处理
            #

            if (

                action["action"] == "read_file"

                and isinstance(result, dict)

                and result.get("success")

            ):

                if "display" in result:

                    console.print(

                        result["display"]

                    )

                else:

                    console.print(

                        result["content"]

                    )

                #
                # 给 LLM 的必须是不带行号源码
                #

                self.memory.add_tool(

                    result["content"]

                )

                continue

            #
            # search_code
            #

            if action["action"] == "search_code":

                console.print(result)

                self.memory.add_tool(

                    str(result)

                )

                continue

            #
            # list_files
            #

            if action["action"] == "list_files":

                console.print(result)

                self.memory.add_tool(

                    str(result)

                )

                continue

            #
            # replace_text
            #

            if action["action"] == "replace_text":

                console.print(result)

                self.memory.add_tool(

                    str(result)

                )

                continue

            #
            # write_file
            #

            if action["action"] == "write_file":

                console.print(result)

                self.memory.add_tool(

                    str(result)

                )

                continue

            #
            # run_python
            #

            if action["action"] == "run_python":

                console.print(result)

                self.memory.add_tool(

                    str(result)

                )

                continue

            #
            # fallback
            #

            console.print(result)

            self.memory.add_tool(

                str(result)

            )

        #
        # 超过最大循环
        #

        console.print()

        console.print(

            "[red]达到最大循环次数[/red]"

        )

        return "达到最大循环次数，任务未完成。"
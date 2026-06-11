from rich.console import Console

from config import MAX_STEPS

from agent.llm import LLM
from agent.parser import Parser
from agent.executor import Executor
from agent.memory import Memory


console = Console()


class AgentLoop:

    def __init__(self):

        self.llm = LLM()
        self.parser = Parser()
        self.executor = Executor()
        self.memory = Memory()

    def run(self, user_input: str):

        self.memory.add_user(user_input)

        current_input = user_input

        modify_keywords = [

            "增加",
            "添加",
            "修改",
            "删除",
            "重构",
            "修复",
            "新增",
            "replace",
            "fix"

        ]

        has_write = False

        for step in range(MAX_STEPS):

            console.print()
            console.print(
                f"[cyan]========== Step {step + 1} ==========[/cyan]"
            )

            response = self.llm.chat(
                current_input,
                history=self.memory.get()
            )

            console.print()
            console.print("[yellow]LLM 输出：[/yellow]")
            console.print(response)

            action = self.parser.parse(response)

            # ------------------------
            # Final Guard
            # ------------------------

            if (
                action.get("action") == "final"
                and any(
                    k in user_input
                    for k in modify_keywords
                )
                and not has_write
            ):

                console.print()
                console.print(
                    "[red]检测到修改任务，但尚未调用 write_file，要求模型继续规划。[/red]"
                )

                current_input = """
用户要求修改代码。

你还没有真正修改文件。

必须：

1. read_file

2. 根据文件生成完整修改版本

3. write_file

4. final

请重新输出 JSON。
"""

                continue

            # ------------------------
            # Final
            # ------------------------

            if action.get("action") == "final":

                answer = action.get("answer", "")

                self.memory.add_assistant(answer)

                console.print()
                console.print("[green]任务完成[/green]")

                return answer

            # ------------------------
            # Tool Execute
            # ------------------------

            if action.get("action") == "write_file":

                has_write = True

            result = self.executor.execute(action)

            console.print()

            if result.get("success"):

                console.print("[green]工具执行成功[/green]")
                console.print(result.get("result"))

            else:

                console.print("[red]工具执行失败[/red]")
                console.print(result.get("error"))

            # Tool 结果反馈给模型

            current_input = f"""
工具执行完成。

Tool:

{action}

Result:

{result}

请根据结果继续下一步。

如果任务已经完成，再输出：

{{
    "action":"final",
    "answer":"..."
}}

否则继续输出下一步 Tool。
"""

        console.print()
        console.print("[red]达到最大执行次数[/red]")

        return "达到最大执行次数，请重新描述任务。"
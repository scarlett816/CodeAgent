from dataclasses import dataclass


@dataclass
class Plan:
    """
    Planner 生成的执行计划
    """

    task_type: str
    description: str
    suggested_steps: list[str]


class Planner:
    """
    Planner

    职责：

    1. 判断是否结束(final)

    2. 根据用户输入生成推荐执行流程

    注意：

    Planner 不直接决定 Tool 参数，
    只负责告诉 Agent 推荐的执行顺序。
    """

    def is_final(self, action: dict) -> bool:

        if not isinstance(action, dict):
            return False

        return action.get("action") == "final"

    def make_plan(self, user_input: str) -> Plan:

        text = user_input.lower()

        # ----------------------------------
        # 读取文件
        # ----------------------------------

        if any(
            keyword in text
            for keyword in [
                "读取",
                "查看",
                "read",
                "显示",
            ]
        ):

            return Plan(

                task_type="read",

                description="读取文件",

                suggested_steps=[

                    "read_file",

                    "final"

                ]

            )

        # ----------------------------------
        # 搜索代码
        # ----------------------------------

        if any(
            keyword in text
            for keyword in [
                "搜索",
                "查找",
                "search",
            ]
        ):

            return Plan(

                task_type="search",

                description="搜索代码",

                suggested_steps=[

                    "search_code",

                    "final"

                ]

            )

        # ----------------------------------
        # 列出文件
        # ----------------------------------

        if any(
            keyword in text
            for keyword in [
                "列出",
                "list",
            ]
        ):

            return Plan(

                task_type="list",

                description="列出文件",

                suggested_steps=[

                    "list_files",

                    "final"

                ]

            )

        # ----------------------------------
        # 运行程序
        # ----------------------------------

        if any(
            keyword in text
            for keyword in [
                "运行",
                "执行",
                "run",
            ]
        ):

            return Plan(

                task_type="run",

                description="运行程序",

                suggested_steps=[

                    "run_python",

                    "final"

                ]

            )

        # ----------------------------------
        # 修改代码
        # ----------------------------------

        if any(
            keyword in text
            for keyword in [

                "增加",

                "添加",

                "修改",

                "删除",

                "重构",

                "替换",

                "append",

                "replace",

                "fix",

                "实现",

            ]
        ):

            return Plan(

                task_type="edit",

                description="修改已有代码",

                suggested_steps=[

                    "read_file",

                    "replace_text",

                    "read_file",

                    "final"

                ]

            )

        # ----------------------------------
        # 默认
        # ----------------------------------

        return Plan(

            task_type="general",

            description="普通任务",

            suggested_steps=[]

        )
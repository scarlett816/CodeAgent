from tools.tool_registry import ToolRegistry


class Executor:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, action):

        name = action.get("action")

        if name == "final":

            return {

                "success": True,

                "final": True,

                "result": action.get("answer", "")

            }

        tool = self.registry.get(name)

        if tool is None:

            return {

                "success": False,

                "final": False,

                "result": f"未知工具：{name}"

            }

        kwargs = {

            k: v

            for k, v in action.items()

            if k != "action"

        }

        try:

            result = tool(**kwargs)

            # Tool 已经返回标准格式
            return result

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }
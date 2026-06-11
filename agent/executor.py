from tools.tool_registry import TOOL_REGISTRY


class Executor:

    def execute(self, action):

        action_name = action.get("action")

        tool = TOOL_REGISTRY.get(action_name)

        if tool is None:

            return {

                "success": False,

                "error": f"未知工具：{action_name}"

            }

        kwargs = {

            k: v

            for k, v in action.items()

            if k != "action"

        }

        try:

            return tool(**kwargs)

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }
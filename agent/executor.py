from mcp.client import MCPClient
from mcp.registry import MCPRegistry
from mcp.servers.filesystem import FilesystemServer

class Executor:
    """
    Executor
    不直接调用 Tool，
    所有请求统一交给 MCP Client。
    """

    def __init__(self):
        registry = MCPRegistry()
        # 注册 Filesystem Server
        registry.register(FilesystemServer())
        self.client = MCPClient(registry)

    def execute(self, action: dict):
        if not isinstance(action, dict):
            return {
                "success": False,
                "error": "action 必须是 dict"
            }

        tool_name = action.get("action")

        if tool_name is None:
            return {
                "success": False,
                "error": "缺少 action"
            }

        kwargs = action.copy()
        kwargs.pop("action", None)

        return self.client.call(
            tool_name,
            **kwargs
        )
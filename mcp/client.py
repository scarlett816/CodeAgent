class MCPClient:

    def __init__(self, registry):
        self.registry = registry
        self.cache = {}

    def call(self, tool_name, **kwargs):
        # ------------------------
        # 优先缓存
        # ------------------------
        if tool_name in self.cache:
            server = self.cache[tool_name]
            return server.call(tool_name,**kwargs)

        # ------------------------
        # 遍历 Server
        # ------------------------

        for server in self.registry.get_servers():
            if server.has_tool(tool_name):
                self.cache[tool_name] = server
                return server.call(tool_name,**kwargs)

        return {
            "success": False,
            "error": f"未找到工具: {tool_name}"
        }
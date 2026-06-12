class MCPRegistry:

    def __init__(self):
        self.servers = []   # 实例变量，一个空列表

    def register(self, server): # 注册方法
        self.servers.append(server)

    def get_servers(self):  # 获取服务器列表的方法
        return self.servers
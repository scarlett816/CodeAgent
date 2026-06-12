class MCPServer:  #定义服务器的基类
    """
    所有 MCP Server 的基类。
    """

    def has_tool(self, tool_name: str) -> bool:#返回布尔值
        """
        是否支持某个工具
        """
        raise NotImplementedError
    # tool_name: str：这是参数注解，表示 tool_name 应该是一个字符串（例如 "read_file"）。
    # 只是提示，不是强制，但能让代码更清晰    
    # raise NotImplementedError：这是一个故意抛出异常的语句。
    # 意思是：这个方法在基类中没有具体实现，任何继承 MCPServer 的子类必须自己重写这个方法，否则一调用就会报错。

    def call(self, tool_name: str, **kwargs):
        """
        调用工具
        """
        raise NotImplementedError
    # **kwargs：这是一个特殊的语法。kwargs 是 “keyword arguments”（关键字参数）的缩写。
    # ** 会把传入的所有 key=value 形式的参数收集成一个字典。

    
# 把基类中的方法想象成一份“合同”。合同上写着“你必须提供 has_tool 和 call 的功能”，但现在还没有具体怎么做。
# 每个具体的服务器（子类）要在自己代码里把这两件事做出来。如果忘了做，程序运行到这里就会抛出 NotImplementedError（未实现错误）来提醒你。
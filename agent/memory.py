class Memory:
    """
    对话记忆

    保存：
        user
        assistant
        tool

    自动裁剪历史长度，避免上下文无限增长。
    """

    def __init__(self):

        self.messages = []

        # 保留最近 30 条消息
        self.max_history = 30

    def trim(self):

        if len(self.messages) > self.max_history:

            self.messages = self.messages[-self.max_history:]

    def add_user(self, text):

        self.messages.append(
            {
                "role": "user",
                "content": str(text)
            }
        )

        self.trim()

    def add_assistant(self, text):

        self.messages.append(
            {
                "role": "assistant",
                "content": str(text)
            }
        )

        self.trim()

    def add_tool(self, text):

        self.messages.append(
            {
                "role": "tool",
                "content": str(text)
            }
        )

        self.trim()

    def get_messages(self):

        return self.messages

    # 兼容旧代码
    def get(self):

        return self.messages

    def clear(self):

        self.messages = []
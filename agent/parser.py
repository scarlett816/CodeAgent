import json


class Parser:
    """
    更健壮的 JSON Parser。

    支持：

    - ```json ... ```
    - Action: {...}
    - 前后解释文字
    - 多个 JSON（取第一个）
    - 普通文本包裹 JSON
    """

    def parse(self, text: str):

        if not text:
            return None

        #
        # 去掉 markdown fence
        #

        text = text.replace("```json", "")
        text = text.replace("```", "")

        #
        # 去掉 Action:
        #

        if text.startswith("Action:"):
            text = text[len("Action:"):].strip()

        #
        # 第一种情况：
        # 整个就是 JSON
        #

        try:
            obj = json.loads(text)

            if isinstance(obj, dict):
                return obj

        except Exception:
            pass

        #
        # 第二种情况：
        # 提取第一个合法 JSON
        #

        start_positions = []

        for i, ch in enumerate(text):

            if ch == "{":

                start_positions.append(i)

        #
        # 没找到
        #

        if not start_positions:

            return None

        #
        # 尝试每一个 {
        #

        for start in start_positions:

            depth = 0

            for end in range(start, len(text)):

                c = text[end]

                if c == "{":

                    depth += 1

                elif c == "}":

                    depth -= 1

                    if depth == 0:

                        candidate = text[start:end + 1]

                        try:

                            obj = json.loads(candidate)

                            if isinstance(obj, dict):

                                return obj

                        except Exception:

                            pass

        #
        # 第三种情况：
        # 行扫描（保险）
        #

        lines = text.splitlines()

        collecting = False

        depth = 0

        buffer = []

        for line in lines:

            if not collecting:

                if "{" in line:

                    collecting = True

                    depth += line.count("{")

                    depth -= line.count("}")

                    buffer.append(line)

                    if depth == 0:

                        try:

                            obj = json.loads("\n".join(buffer))

                            return obj

                        except Exception:

                            buffer = []
                            collecting = False

            else:

                buffer.append(line)

                depth += line.count("{")

                depth -= line.count("}")

                if depth == 0:

                    candidate = "\n".join(buffer)

                    try:

                        obj = json.loads(candidate)

                        if isinstance(obj, dict):

                            return obj

                    except Exception:

                        pass

                    buffer = []

                    collecting = False

        #
        # 全失败
        #

        return None
import json
import re
import ast


class Parser:
    """
    容错 JSON Parser

    支持：

    1. 标准 JSON
    2. ```json ... ```
    3. ``` ... ```
    4. Python dict
    5. 单引号
    6. True False None
    7. 尾逗号
    8. new/content 中未转义换行
    """

    def parse(self, text):

        if text is None:
            return None

        text = str(text).strip()

        #
        # 去掉 markdown
        #

        text = self._remove_markdown(text)

        #
        # 提取第一个 {}
        #

        text = self._extract_json(text)

        if text is None:
            return None

        #
        # 第一轮
        #

        obj = self._try_json(text)

        if obj is not None:
            return obj

        #
        # 修复换行
        #

        text2 = self._escape_multiline_string(text)

        obj = self._try_json(text2)

        if obj is not None:
            return obj

        #
        # 修复 True False None
        #

        text3 = (

            text2

            .replace("True", "true")

            .replace("False", "false")

            .replace("None", "null")

        )

        obj = self._try_json(text3)

        if obj is not None:
            return obj

        #
        # 修复尾逗号
        #

        text4 = re.sub(

            r",\s*}",

            "}",

            text3

        )

        text4 = re.sub(

            r",\s*]",

            "]",

            text4

        )

        obj = self._try_json(text4)

        if obj is not None:
            return obj

        #
        # Python dict
        #

        try:

            return ast.literal_eval(text)

        except Exception:

            pass

        #
        # 单引号 dict
        #

        try:

            return ast.literal_eval(text4)

        except Exception:

            pass

        return None

    #
    # -------------------------
    #

    def _try_json(self, text):

        try:

            return json.loads(text)

        except Exception:

            return None

    #
    # -------------------------
    #

    def _remove_markdown(self, text):

        m = re.search(

            r"```json\s*(.*?)```",

            text,

            re.S | re.I

        )

        if m:

            return m.group(1).strip()

        m = re.search(

            r"```\s*(.*?)```",

            text,

            re.S

        )

        if m:

            return m.group(1).strip()

        return text

    #
    # -------------------------
    #

    def _extract_json(self, text):

        start = text.find("{")

        end = text.rfind("}")

        if start == -1 or end == -1:

            return None

        return text[start:end + 1]

    #
    # -------------------------
    #

    def _escape_multiline_string(self, text):
        """
        自动修复

        "new": "
        def logout():
            pass
        "

        →

        "new":"\\ndef logout():\\n    pass"
        """

        result = []

        in_string = False

        escape = False

        for ch in text:

            if escape:

                result.append(ch)

                escape = False

                continue

            if ch == "\\":

                result.append(ch)

                escape = True

                continue

            if ch == '"':

                result.append(ch)

                in_string = not in_string

                continue

            if in_string:

                if ch == "\n":

                    result.append("\\n")

                    continue

                if ch == "\r":

                    continue

                if ch == "\t":

                    result.append("\\t")

                    continue

            result.append(ch)

        return "".join(result)
import json
import re


class Parser:
    """
    从 LLM 输出中提取 JSON Action。
    """

    def parse(self, text: str) -> dict:
        text = text.strip()

        # 去掉 markdown json 代码块
        text = re.sub(r"^```json", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"^```", "", text).strip()
        text = re.sub(r"```$", "", text).strip()

        # 提取第一个 JSON
        match = re.search(r"\{[\s\S]*\}", text)

        if match is None:
            return {
                "action": "final",
                "answer": text
            }

        json_text = match.group()

        try:
            return json.loads(json_text)

        except Exception:
            return {
                "action": "final",
                "answer": text
            }
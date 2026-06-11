import requests

from config import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)

from prompts import SYSTEM_PROMPT


class LLM:

    def __init__(self):

        self.url = OLLAMA_BASE_URL

        self.model = OLLAMA_MODEL

    def chat(
        self,
        user_message,
        history=None
    ):

        if history is None:
            history = []

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(history)

        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        payload = {

            "model": self.model,

            "messages": messages,

            "stream": False

        }

        response = requests.post(
            self.url,
            json=payload,
            timeout=600
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]
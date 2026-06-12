import requests
from config import (OLLAMA_BASE_URL,OLLAMA_MODEL,)

class LLM:
    def __init__(self):
        self.url = OLLAMA_BASE_URL
        self.model = OLLAMA_MODEL

    def chat(self, messages):
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
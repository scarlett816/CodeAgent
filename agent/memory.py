import json
import os

from config import HISTORY_FILE


class Memory:

    def __init__(self):

        self.history = []

        self.load()

    def add_user(self, text):

        self.history.append(
            {
                "role": "user",
                "content": text
            }
        )

    def add_assistant(self, text):

        self.history.append(
            {
                "role": "assistant",
                "content": text
            }
        )

    def get(self):

        return self.history

    def clear(self):

        self.history = []

        self.save()

    def save(self):

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.history,
                f,
                ensure_ascii=False,
                indent=4
            )

    def load(self):

        if not os.path.exists(HISTORY_FILE):
            return

        try:

            with open(
                HISTORY_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                self.history = json.load(f)

        except:

            self.history = []
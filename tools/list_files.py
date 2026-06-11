import os

from config import WORKSPACE


IGNORE_DIRS = {

    "__pycache__",

    ".git",

    ".idea",

    ".vscode",

    "venv",

    "logs",

    "memory"

}


def list_files():

    result = []

    for root, dirs, files in os.walk(WORKSPACE):

        dirs[:] = [

            d

            for d in dirs

            if d not in IGNORE_DIRS

        ]

        for file in files:

            path = os.path.join(

                root,

                file

            )

            rel = os.path.relpath(

                path,

                WORKSPACE

            )

            result.append(rel)

    result.sort()

    return result
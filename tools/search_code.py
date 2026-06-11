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


def search_code(keyword: str):

    result = []

    for root, dirs, files in os.walk(WORKSPACE):

        dirs[:] = [

            d

            for d in dirs

            if d not in IGNORE_DIRS

        ]

        for file in files:

            if not file.endswith(".py"):

                continue

            path = os.path.join(

                root,

                file

            )

            try:

                with open(

                    path,

                    "r",

                    encoding="utf-8"

                ) as f:

                    lines = f.readlines()

            except:

                continue

            for idx, line in enumerate(lines):

                if keyword.lower() in line.lower():

                    start = max(

                        0,

                        idx - 1

                    )

                    end = min(

                        len(lines),

                        idx + 2

                    )

                    context = "".join(

                        lines[start:end]

                    )

                    result.append(

                        {

                            "file":

                                os.path.relpath(

                                    path,

                                    WORKSPACE

                                ),

                            "line":

                                idx + 1,

                            "text":

                                line.strip(),

                            "context":

                                context

                        }

                    )

    return result
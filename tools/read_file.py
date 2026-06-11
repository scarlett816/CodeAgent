from config import WORKSPACE


def read_file(path, max_chars=12000):

    try:

        file_path = WORKSPACE / path

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read()

        if len(content) > max_chars:

            content = content[:max_chars]

        return {

            "success": True,

            "result": content

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
from config import WORKSPACE


def write_file(path, content):

    try:

        file_path = WORKSPACE / path

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(content)

        return {

            "success": True,

            "result": {

                "message": "文件写入成功",

                "path": path,

                "chars": len(content)

            }

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
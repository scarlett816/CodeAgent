from pathlib import Path
import shutil

from config import WORKSPACE


def replace_text(
    path: str,
    old: str = "",
    new: str = "",
    mode: str = "replace",
):
    """
    修改已有文件。

    mode:

        replace
            old -> new

        insert_after
            old + new

        insert_before
            new + old

        append
            文件末尾追加 new

        prepend
            文件开头插入 new
    """

    file_path = Path(WORKSPACE) / path

    if not file_path.exists():

        return {

            "success": False,

            "error": f"{path} 不存在"

        }

    try:

        content = file_path.read_text(

            encoding="utf-8"

        )

        original = content

        #
        # replace
        #

        if mode == "replace":

            if old not in content:

                return {

                    "success": False,

                    "error": "未找到需要替换的内容"

                }

            content = content.replace(

                old,

                new,

                1

            )

        #
        # insert_after
        #

        elif mode == "insert_after":

            if old not in content:

                return {

                    "success": False,

                    "error": "未找到插入位置"

                }

            content = content.replace(

                old,

                old + new,

                1

            )

        #
        # insert_before
        #

        elif mode == "insert_before":

            if old not in content:

                return {

                    "success": False,

                    "error": "未找到插入位置"

                }

            content = content.replace(

                old,

                new + old,

                1

            )

        #
        # append
        #

        elif mode == "append":

            if not content.endswith("\n"):

                content += "\n"

            content += new

        #
        # prepend
        #

        elif mode == "prepend":

            content = new + content

        else:

            return {

                "success": False,

                "error": f"未知 mode: {mode}"

            }

        #
        # 没变化
        #

        if content == original:

            return {

                "success": False,

                "error": "文件内容没有变化"

            }

        #
        # backup
        #

        backup_path = file_path.with_suffix(

            file_path.suffix + ".bak"

        )

        shutil.copyfile(

            file_path,

            backup_path

        )

        #
        # write
        #

        file_path.write_text(

            content,

            encoding="utf-8"

        )

        return {

            "success": True,

            "path": path,

            "mode": mode,

            "backup": str(backup_path),

            "size": len(content)

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
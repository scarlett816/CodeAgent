from pathlib import Path
import shutil

from config import WORKSPACE


def write_file(
    path: str,
    content: str,
    overwrite: bool = False,
):
    """
    写入文件。

    默认：
        已存在文件禁止覆盖。

    如需覆盖：
        overwrite=True

    返回统一 dict。
    """

    file_path = Path(WORKSPACE) / path

    try:

        # 自动创建目录
        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # 已存在文件
        #

        if file_path.exists():

            #
            # 默认拒绝覆盖
            #

            if not overwrite:

                return {

                    "success": False,

                    "error":
                        (
                            f"{path} 已存在。"
                            "请优先使用 replace_text 修改，"
                            "或显式传入 overwrite=True。"
                        )

                }

            #
            # 自动备份
            #

            backup_path = file_path.with_suffix(

                file_path.suffix + ".bak"

            )

            shutil.copyfile(

                file_path,

                backup_path

            )

        #
        # 写入
        #

        file_path.write_text(

            content,

            encoding="utf-8"

        )

        return {

            "success": True,

            "path": path,

            "overwrite": overwrite,

            "backup": file_path.exists(),

            "size": len(content)

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
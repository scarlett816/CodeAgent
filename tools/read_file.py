from pathlib import Path

from config import WORKSPACE


def read_file(path: str):
    """
    读取文件内容。

    返回：
        - success: True / False
        - content: 原始源码（不给 LLM 加行号）
        - display: 带行号版本（给终端打印）
    """

    file_path = Path(WORKSPACE) / path

    if not file_path.exists():
        return {
            "success": False,
            "error": f"文件不存在：{path}"
        }

    if not file_path.is_file():
        return {
            "success": False,
            "error": f"不是文件：{path}"
        }

    try:
        content = file_path.read_text(
            encoding="utf-8"
        )

    except UnicodeDecodeError:

        content = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    # ---------- 仅用于终端显示 ----------
    display_lines = []

    for idx, line in enumerate(content.splitlines(), start=1):

        display_lines.append(
            f"{idx:4d} | {line}"
        )

    display = "\n".join(display_lines)

    return {

        # 是否成功
        "success": True,

        # 给 LLM 使用（不要带行号）
        "content": content,

        # 给终端打印
        "display": display,

        # 一些附加信息
        "path": path,

        "line_count": len(content.splitlines()),

        "char_count": len(content)

    }
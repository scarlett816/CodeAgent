from mcp.base import MCPServer

from tools.read_file import read_file
from tools.write_file import write_file
from tools.replace_text import replace_text
from tools.search_code import search_code
from tools.run_python import run_python
from tools.list_files import list_files

class FilesystemServer(MCPServer):
    """
    Filesystem MCP Server
    使用 tool_map 动态注册工具，
    不再使用大量 if/elif。
    """

    def __init__(self):
        self.tool_map = {
            "read_file": self._read_file,
            "write_file": self._write_file,
            "replace_text": self._replace_text,
            "search_code": self._search_code,
            "run_python": self._run_python,
            "list_files": self._list_files,
        }

    def has_tool(self, tool_name: str):
        return tool_name in self.tool_map

    def call(self, tool_name: str, **kwargs):
        func = self.tool_map.get(tool_name)
        if func is None:
            return {
                "success": False,
                "error": f"FilesystemServer 不支持工具: {tool_name}"
            }

        try:
            return func(**kwargs)
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    # Tool Wrapper

    def _read_file(self, **kwargs):
        return read_file(kwargs["path"])

    def _write_file(self, **kwargs):
        return write_file(
            path=kwargs["path"],
            content=kwargs["content"],
            overwrite=kwargs.get(
                "overwrite",
                False
            )
        )

    def _replace_text(self, **kwargs):
        return replace_text(
            path=kwargs["path"],
            old=kwargs.get(
                "old",
                ""
            ),

            new=kwargs.get(
                "new",
                ""
            ),

            mode=kwargs.get(
                "mode",
                "replace"
            )
        )

    def _search_code(self, **kwargs):
        return search_code(kwargs["keyword"])

    def _run_python(self, **kwargs):
        return run_python(kwargs["path"])

    def _list_files(self, **kwargs):
        return list_files()
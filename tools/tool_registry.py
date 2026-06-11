from tools.read_file import read_file
from tools.write_file import write_file
from tools.list_files import list_files
from tools.search_code import search_code
from tools.run_python import run_python


class ToolRegistry:

    def __init__(self):

        self.tools = {

            "read_file": read_file,

            "write_file": write_file,

            "list_files": list_files,

            "search_code": search_code,

            "run_python": run_python,

        }

    def get(self, name):

        return self.tools.get(name)
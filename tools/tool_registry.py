from tools.read_file import read_file
from tools.write_file import write_file
from tools.list_files import list_files
from tools.search_code import search_code
from tools.run_python import run_python
from tools.replace_text import replace_text


TOOL_REGISTRY = {

    "read_file": read_file,

    "write_file": write_file,

    "replace_text": replace_text,

    "list_files": list_files,

    "search_code": search_code,

    "run_python": run_python,

}
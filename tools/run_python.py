import subprocess

from config import WORKSPACE


def run_python(path):

    try:

        file_path = WORKSPACE / path

        result = subprocess.run(

            [

                "python",

                str(file_path)

            ],

            capture_output=True,

            text=True,

            timeout=30

        )

        return {

            "success": True,

            "result": {

                "stdout": result.stdout,

                "stderr": result.stderr,

                "returncode": result.returncode

            }

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }
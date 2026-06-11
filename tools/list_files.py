from config import WORKSPACE


def list_files():

    files = []

    for path in WORKSPACE.rglob("*"):

        if path.is_file():

            files.append(

                str(

                    path.relative_to(WORKSPACE)

                )

            )

    return {

        "success": True,

        "result": files

    }
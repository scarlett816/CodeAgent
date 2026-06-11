from config import WORKSPACE


def search_code(keyword: str):

    matches = []

    for path in WORKSPACE.rglob("*.py"):

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                lines = f.readlines()

            for idx, line in enumerate(lines):

                if keyword.lower() in line.lower():

                    start = max(0, idx - 1)
                    end = min(len(lines), idx + 2)

                    context = "".join(lines[start:end])

                    matches.append(
                        {
                            "file": str(
                                path.relative_to(WORKSPACE)
                            ),
                            "line": idx + 1,
                            "text": line.strip(),
                            "context": context
                        }
                    )

                    if len(matches) >= 20:
                        break

        except Exception:
            pass

        if len(matches) >= 20:
            break

    return {
        "success": True,
        "result": matches
    }
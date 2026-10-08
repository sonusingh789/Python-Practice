import subprocess
import sys
from pathlib import Path

import nbformat


def main() -> int:
    result = subprocess.run(
        ["git", "ls-files", "--", "*.ipynb"],
        check=True,
        capture_output=True,
        text=True,
    )
    notebook_paths = [
        Path(path)
        for path in result.stdout.splitlines()
        if path
    ]
    failures = []

    for path in notebook_paths:
        try:
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
        except (OSError, nbformat.ValidationError, nbformat.reader.NotJSONError) as error:
            failures.append(f"{path}: {error}")

    if failures:
        print("Notebook validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Validated {len(notebook_paths)} notebook(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

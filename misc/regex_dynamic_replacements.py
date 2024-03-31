from __future__ import annotations

import re
from typing import Match

# with open("src.py") as f:
#     contents = f.read()
contents = """
import os  # noqa: F401

print('hello demo')  # noqa

# another comment here
"""


def cb(match: Match[str]) -> str:
    return f'{match[1]}{len(match[2]) * "."}'


def main() -> None:
    comment = re.compile("(# ?)([^\n]+)")

    print(comment.sub(cb, contents), end="")


if __name__ == "__main__":
    main()

import subprocess
from typing import Final, Literal, overload


@overload
def output(*cmd: str, text: Literal[True]) -> str: ...
@overload
def output(*cmd: str, text: Literal[False] = False) -> bytes: ...


def output(*cmd: str, text: bool = False) -> bytes | str:
    return subprocess.check_output(cmd, text=text)


# this is the same
# Literal['passed'] | Literal['failed'] | Literal['errored']
# Literal['passed', 'failed', 'errored']

PASSED: Literal["passed"] = "passed"
FAILED: Final = "passed"  # Final implicitly applies Literal (not found in the docs :))


def report_status(status: Literal["passed", "failed", "errored"]) -> ...:
    pass


def main() -> None:
    print(output("echo", "hi"))
    print(output("echo", "hi", text=True))

    report_status("passed")
    report_status(PASSED)
    report_status(FAILED)


if __name__ == "__main__":
    main()

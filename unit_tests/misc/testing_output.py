import subprocess
import sys


# capsys captures output at the process level, it can't capture
# subprocesses output, capfd can but it's less lightweight
def test_hello(capsys):
    hello("someone")
    stdout, stderr = capsys.readouterr()
    assert stdout == "hello hello someone\n"
    hello("someone else")
    stdout, stderr = capsys.readouterr()
    assert stdout == "hello hello someone else\n"


def hello(name: str) -> None:
    print(f"hello hello {name}")


def hello2(name: str) -> None:
    subprocess.check_call(("echo", "hello", "hello", name))
    print(f"hello hello {name}")


def main() -> None:
    hello(sys.argv[1])
    hello2(sys.argv[1])


if __name__ == "__main__":
    main()

import os
from unittest import mock

# the first approach is to use pytest-env plugin


def greet() -> None:
    username = os.environ["USER"]  # probably use getpass.getuser() instead
    print(f"hello hello, {username}")


def main() -> int:
    greet()
    return 0


# the second approach is to use monkeypatch
# note that monkeypatch tears down (and USER env var is unset)
# at _some_ point later
def test_greet(capsys, monkeypatch):
    monkeypatch.setenv("USER", "nobody2")
    greet()
    out, err = capsys.readouterr()
    assert out == "hello hello, nobody2\n"


# the third approach is to use unittest.mock
def test_greet2(capsys):
    with mock.patch.dict(os.environ, {"USER": "nobody3"}):
        greet()

    out, err = capsys.readouterr()
    assert out == "hello hello, nobody3\n"


if __name__ == "__main__":
    raise SystemExit(main())

import os.path
import tempfile

SOME_FILE = "foo.txt"


def main() -> None:
    fd, temp_path = tempfile.mkstemp(dir=os.path.dirname(SOME_FILE))
    try:
        with open(fd, "w") as f:
            f.write("these are the new contents\n")
        os.replace(temp_path, SOME_FILE)
    except BaseException:
        os.remove(temp_path)
        raise


if __name__ == "__main__":
    main()

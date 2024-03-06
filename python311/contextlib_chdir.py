import contextlib
import os


def main() -> None:
    print(os.getcwd())
    # not thread-safe, async-safe etc
    with contextlib.chdir("C:/Users"):
        print(os.getcwd())
    print(os.getcwd())


if __name__ == "__main__":
    main()

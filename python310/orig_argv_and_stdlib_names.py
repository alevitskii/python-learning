import sys


def main() -> None:
    print(sys.stdlib_module_names)
    print(sys.argv)
    print(sys.orig_argv)


if __name__ == "__main__":
    main()

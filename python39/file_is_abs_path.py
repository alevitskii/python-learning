import os.path


def main() -> None:
    print(f"my file is {__file__}")
    my_parent_dir = os.path.normpath(os.path.join(__file__, ".."))
    print(my_parent_dir)


if __name__ == "__main__":
    main()

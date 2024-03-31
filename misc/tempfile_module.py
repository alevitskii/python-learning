import tempfile


def main() -> None:
    # it's sometimes easier to create a temp dir and create
    # files inside it with open, because when you write to
    # a temp file you need to call flush for the content to appear on disk
    with tempfile.TemporaryDirectory() as tmpdir:
        print(tmpdir)

    # on Unix platforms TemporaryFile doesn't create an actual
    # file on the filesystem. Use NamedTemporaryFile if you
    # need a file
    with tempfile.TemporaryFile() as tmpfile:
        print(tmpfile)
        print(tmpfile.name)

    with tempfile.NamedTemporaryFile() as tmpfile:
        print(tmpfile)
        print(tmpfile.name)


if __name__ == "__main__":
    main()

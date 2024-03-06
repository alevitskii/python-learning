import sys


def main() -> None:
    try:
        raise AssertionError("hi")
    except Exception:
        tp, value, tb = sys.exc_info()
        print(f"{tp!r}, {value!r}, {tb!r}")
        # you can actually get additional info from just the value
        print(f"{type(value)!r}, {value!r}, {value.__traceback__!r}")

        # sys.exception is added to get only value, exc_info is soft deprecated
        value = sys.exception()
        print(f"{type(value)!r}, {value!r}, {value.__traceback__!r}")


if __name__ == "__main__":
    main()

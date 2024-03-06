import contextlib


@contextlib.contextmanager
def ctx_very_very_very_very_very_very_very_very_very_very_very_very_long():
    yield 1


def main() -> None:
    with (
        ctx_very_very_very_very_very_very_very_very_very_very_very_very_long() as v1,
        ctx_very_very_very_very_very_very_very_very_very_very_very_very_long() as v2,
    ):
        print(v1, v2)


if __name__ == "__main__":
    main()

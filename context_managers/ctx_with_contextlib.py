# THE EASIER WAY TO SET UP A CONTEXT MANAGER

import contextlib
from collections.abc import Generator


class FooError(RuntimeError):
    pass


@contextlib.contextmanager
def my_ctx() -> Generator[tuple[int, int], None, None]:
    print("before")
    try:
        yield (42, 99)
        # in some cases you want to put after in the finally block
        print("after")
    except FooError as inst:
        print(f"supressing {inst=}")
    except BaseException as inst:
        # it'll work ok without this except, it's here for clarity
        print(f"not supressing {inst=}")
        raise


def main() -> None:
    with my_ctx() as (x1, x2):
        print("inside")
        print(f"{x1=} {x2=}")

    # ctx = my_ctx()
    # print("before ctx")
    # with ctx:
    #     print("boom")
    #     # raise RuntimeError("wat")
    #     raise FooError()


if __name__ == "__main__":
    main()

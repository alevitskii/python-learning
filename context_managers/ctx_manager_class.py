# THE HARD WAY TO SET UP A CONTEXT MANAGER

import sys
from types import TracebackType


class FooError(RuntimeError):
    pass


class Ctx:
    def __init__(self) -> None:
        # it's best to not have any side effects in init method
        # leave it to enter
        print("initialization")

    def __enter__(self) -> tuple[int, int]:
        # acquire resourses, open connections, modify global variables etc
        print("before")
        return (42, 99)

    def __exit__(
        self,
        tp: type[BaseException] | None,
        inst: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None:
        print("after")
        if isinstance(inst, FooError):
            print(f"supressing {inst=}")
            return True
        print(f"not supressing {inst=}")
        return False  # or None (or any falsy?)


def main() -> None:
    # with Ctx() as (x1, x2):
    #     print("inside")
    #     print(f"{x1=} {x2=}")

    # ctx = Ctx()
    # print("before ctx")
    # with ctx:
    #     print("boom")
    #     # raise FooError()
    #     raise RuntimeError("wat")

    # this is kind of the way it works
    ctx = Ctx()
    print("before ctx")
    __enter__ = type(ctx).__enter__
    __exit__ = type(ctx).__exit__
    try:
        _ = __enter__(ctx)
        print("boom")
        # raise RuntimeError("wat")
        raise FooError()
    except BaseException:
        suppressed = __exit__(ctx, *sys.exc_info())
        if not suppressed:
            raise
    else:
        __exit__(ctx, None, None, None)


if __name__ == "__main__":
    main()

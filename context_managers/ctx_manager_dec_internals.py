import contextlib
from collections.abc import Callable, Generator
from types import TracebackType


class _MyContextManager[TRet]:
    def __init__(self, gen: Generator[TRet, None, None]) -> None:
        self.gen = gen

    def __enter__(self) -> TRet:
        try:
            return next(self.gen)
        except StopIteration:
            raise RuntimeError("generator did not yield")

    def __exit__(
        self,
        tp: type[BaseException] | None,
        inst: BaseException | None,
        tb: TracebackType | None,
    ) -> bool | None:
        if tp is None:
            try:
                next(self.gen)
            except StopIteration:
                return None
            else:
                raise RuntimeError("generator did not stop")
        else:
            try:
                # not sure how fix this
                self.gen.throw(inst)
            except StopIteration as e:
                if inst is e:
                    return False
                return True
            except BaseException as e:
                if inst is e:
                    return False
                else:
                    raise


def my_contextmanager[
    TRet
](func: Callable[..., Generator[TRet, None, None]]) -> Callable[..., contextlib.AbstractContextManager[TRet]]:
    def my_contextmanager_callable(*args, **kwargs) -> contextlib.AbstractContextManager[TRet]:
        return _MyContextManager(func(*args, **kwargs))

    return my_contextmanager_callable


class FooError(RuntimeError):
    pass


@my_contextmanager
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
    # with my_ctx() as (x1, x2):
    #     print("inside")
    #     print(f"{x1=} {x2=}")

    ctx = my_ctx()
    print("before ctx")
    with ctx:
        print("boom")
        raise RuntimeError("wat")
        # raise StopIteration("wat")
        # raise FooError()


if __name__ == "__main__":
    main()

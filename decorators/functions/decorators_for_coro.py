# wrapped should be of the same type as callable, i.e. func -> func, coro -> coro
import asyncio
import time
from collections.abc import Awaitable, Callable
from functools import wraps
from typing import TypedDict

X, Y = 1, 2


# 1st example
def decorator[R](callable: Callable[[int, int], R]) -> Callable[[], R]:
    """Call <callable> with fixed values"""

    @wraps(callable)
    def wrapped() -> R:
        return callable(X, Y)

    return wrapped


@decorator
def func(x: int, y: int) -> int:
    return x + y


@decorator
async def coro(x: int, y: int) -> int:
    return x + y


class Result[R](TypedDict):
    latency: float
    result: R


# I didn't manage to type annonate single `timing` function.
# Splitting them into sync and async versions solved the problem.

# @overload
# def timing[**P, R](callable: Callable[P, R]) -> Callable[P, Result[R]]: ...


# @overload
# def timing[**P, R](
#     callable: Callable[P, Awaitable[R]],
# ) -> Callable[P, Awaitable[Result[R]]]: ...


# # 2nd example
# def timing[**P, R](
#     callable: Callable[P, R] | Callable[P, Awaitable[R]],
# ) -> Callable[P, Result[R]] | Callable[P, Awaitable[Result[R]]]:
#     @wraps(callable)
#     def wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[R]:
#         start = time.time()
#         # For some reason overload doesn't help distinguish between the two callbacks
#         callable_ = cast(Callable[P, R], callable)
#         result = callable_(*args, **kwargs)
#         # result = callable(*args, **kwargs)
#         latency = time.time() - start
#         return {"latency": latency, "result": result}

#     @wraps(callable)
#     async def wrapped_coro(*args: P.args, **kwargs: P.kwargs) -> Result[R]:
#         start = time.time()
#         callable_ = cast(Callable[P, Awaitable[R]], callable)
#         result = await callable_(*args, **kwargs)
#         # result = await callable(*args, **kwargs)
#         latency = time.time() - start
#         return {"latency": latency, "result": result}

#     if inspect.iscoroutinefunction(callable):
#         return wrapped_coro

#     return wrapped


# 2nd example
def timing[**P, R](callable: Callable[P, R]) -> Callable[P, Result[R]]:
    @wraps(callable)
    def wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[R]:
        start = time.time()
        result = callable(*args, **kwargs)
        latency = time.time() - start
        return {"latency": latency, "result": result}

    return wrapped


# 2nd example
def timing_async[**P, R](
    callable: Callable[P, Awaitable[R]],
) -> Callable[P, Awaitable[Result[R]]]:
    @wraps(callable)
    async def wrapped(*args: P.args, **kwargs: P.kwargs) -> Result[R]:
        start = time.time()
        result = await callable(*args, **kwargs)
        latency = time.time() - start
        return {"latency": latency, "result": result}

    return wrapped


@timing
def func2() -> int:
    time.sleep(0.1)
    return 42


@timing_async
async def coro2() -> int:
    await asyncio.sleep(0.1)
    return 42


async def run() -> None:
    coro = coro2()
    print(coro)
    res = await coro
    print(res)


def main() -> None:
    # 1st example
    print(func())
    print(coro())
    # 2nd example
    print(func2())
    asyncio.run(run())


if __name__ == "__main__":
    main()

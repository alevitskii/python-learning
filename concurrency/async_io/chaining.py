import asyncio
from asyncio import Future
from collections.abc import Generator


# yield from
def coro3_yield_from(k: int) -> Future[int]:
    future = asyncio.get_running_loop().create_future()
    future.set_result(k + 3)
    return future


def coro2_yield_from(j: int) -> Generator[None, None, int]:
    j = j * j
    result = yield from coro3_yield_from(j)
    return result


def coro1_yield_from() -> Generator[None]:
    i = 0
    while i < 100:
        final_result = yield from coro2_yield_from(i)
        print(f"f(i) = {final_result}")
        i += 1


# async
async def coro3_async(k: int) -> int:
    return k + 3


async def coro2_async(j: int) -> int:
    j = j * j
    res = await coro3_async(j)
    return res


async def coro1_async() -> None:
    i = 0
    while i < 100:
        res = await coro2_async(i)
        print(f"f({i}) = {res}")
        i += 1


def main() -> None:
    asyncio.run(coro1_async())
    # Generator-based coroutine, THIS DOESN'T WORK WITH `yield from` ANYMORE
    # asyncio.run(coro1_yield_from())


if __name__ == "__main__":
    main()

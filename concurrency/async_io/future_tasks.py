import asyncio
from asyncio import Future


async def bar(future: Future[str]) -> None:
    print("bar will sleep for 3 seconds")
    await asyncio.sleep(3)
    print("bar resolving the future")
    future.set_result("future is resolved")


async def foo(future: Future[str]) -> None:
    print("foo will await the future")
    await future
    print("foo finds the future resolved")


async def run1() -> None:
    future: Future[str] = Future()
    _ = await asyncio.gather(foo(future), bar(future))


async def run2() -> None:
    future: Future[str] = Future()

    t1 = asyncio.create_task(bar(future))
    t2 = asyncio.create_task(foo(future))

    await t1
    await t2


def main() -> None:
    asyncio.run(run1())
    print("main exiting")


if __name__ == "__main__":
    main()

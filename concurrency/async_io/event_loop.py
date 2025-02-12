import asyncio
import time
from asyncio import Future
from threading import current_thread

shutdown = False


# sync call is blocking the loop
def resolver_blocking(future: Future[None]) -> None:
    print(
        f"[resolver_blocking] Is loop running in thread {current_thread().name} = {asyncio.get_event_loop().is_running()}\n"
    )

    time.sleep(10)
    future.set_result(None)


# async call is not blocking the loop
async def resolver_non_blocking(future: Future[None]) -> None:
    print(
        f"[resolver_non_blocking] Is loop running in thread {current_thread().name} = {asyncio.get_event_loop().is_running()}\n"
    )
    await asyncio.sleep(10)
    future.set_result(None)


async def monitor_coro() -> None:
    global shutdown

    while shutdown is False:
        print(f"Alive at {time.time()}")
        await asyncio.sleep(1)


async def coro() -> None:
    global shutdown

    print("coro running")
    future: Future[None] = Future()

    loop = asyncio.get_event_loop()
    monitor_coro_future = asyncio.ensure_future(monitor_coro())
    # loop.call_later(5, resolver_blocking, future)
    resolver_future = asyncio.ensure_future(resolver_non_blocking(future))

    print(
        f"[coro] Is loop running in thread {current_thread().name} = {loop.is_running()}\n"
    )

    await future
    print("[coro] awaiting 2 seconds")
    await asyncio.sleep(2)
    shutdown = True

    await resolver_future
    await monitor_coro_future


def main() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print(
        f"[main] Is loop running in thread {current_thread().name} = {loop.is_running()}\n"
    )

    try:
        loop.run_until_complete(coro())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()

    print("main exiting")


if __name__ == "__main__":
    main()

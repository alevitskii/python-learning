import asyncio
import time
from asyncio import Future
from threading import Thread, current_thread

# First option


async def asleep(sleep_for: int) -> None:
    current_loop = asyncio.get_running_loop()
    future = current_loop.create_future()
    Thread(target=sync_sleep, args=(sleep_for, future)).start()
    await future


def sync_sleep(sleep_for: int, future: Future[None]) -> None:
    # sleep synchronously
    time.sleep(sleep_for)

    # define a nested coroutine to resolve the future
    async def sleep_future_resolver() -> None:
        # resolve the future
        future.set_result(None)

    # Future is not thread-safe, that's why we use run_coroutine_threadsafe
    asyncio.run_coroutine_threadsafe(sleep_future_resolver(), future.get_loop())
    print(f"Sleeping completed in {current_thread().name}\n", flush=True)


async def run() -> None:
    work = []
    work.append(asleep(5))
    work.append(asleep(5))
    work.append(asleep(5))
    work.append(asleep(5))
    work.append(asleep(5))

    await asyncio.gather(*work)


# Second option


def sync_sleep2(sleep_for: int) -> None:
    # sleep synchronously
    time.sleep(sleep_for)
    print(f"Sleeping completed in {current_thread().name}\n", flush=True)


async def run2() -> None:
    work = []
    work.append(asyncio.to_thread(sync_sleep2, 5))
    work.append(asyncio.to_thread(sync_sleep2, 5))
    work.append(asyncio.to_thread(sync_sleep2, 5))
    work.append(asyncio.to_thread(sync_sleep2, 5))
    work.append(asyncio.to_thread(sync_sleep2, 5))

    await asyncio.gather(*work)


def main() -> None:
    start = time.time()
    asyncio.run(run2())
    print(f"main program exiting after running for {time.time() - start}")


if __name__ == "__main__":
    main()

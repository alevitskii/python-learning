import asyncio
import os
import random
import time
from collections.abc import Sequence

type Item = tuple[str, float]


async def makeitem(size: int = 5) -> str:
    return os.urandom(size).hex()


async def randsleep(caller: str = "") -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue[Item]) -> None:
    n = random.randint(0, 10)
    for _ in range(n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue[Item]) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}> in {now - t:0.5f} seconds.")
        q.task_done()


async def run(nprod: int, ncon: int) -> None:
    q: asyncio.Queue[Item] = asyncio.Queue()

    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]

    await asyncio.gather(*producers)
    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


def main(args: Sequence[str] | None = None) -> None:
    import argparse

    random.seed(444)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args(args)

    start = time.perf_counter()
    asyncio.run(run(**vars(ns)))
    elapsed = time.perf_counter() - start

    print(f"Program completed in {elapsed:0.5f} seconds.")


if __name__ == "__main__":
    main()

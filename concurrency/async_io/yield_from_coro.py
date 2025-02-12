# NOTE: asyncio.coroutine is removed since 3.11, use async.
# However @types.coroutine is still there and works OK,
# but it works slightly differently from asyncio.coroutine - asyncio.coroutine can
# make an ordinary function a coroutine and compatible with native coros while
# the one from types can't.

# Previously there were generator-based coroutines and native coroutines.
# Generator-based had to have @asyncio.coroutine and `yield from` inside
# in order to work with native coroutines. Now you should use native coroutines.

# - generators are used to refer to functions that only produce values;
# - vanilla coroutines only receive values;
# - generator-based coroutines are identified via the presence of `yield from` in the method body;
# - native coroutines are defined using the async/await syntax.

# Awaitable objects must implement the __await__() method that should return an iterator.

# Any class that implements the iteration protocol can appear on the right-hand side of a `yield from` expression.

import asyncio
import time
import types
from collections.abc import Generator
from threading import current_thread

# asyncio.coroutine was removed from Python
"""
# hello_routine isn't a traditional generator that returns items in a sequence
@asyncio.coroutine
def hello_routine():
    print("hello world")

# coro becomes a generator-based coroutine itself on account of using the `yield from` expression
def coro():
    yield from hello_routine()
"""


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
@asyncio.coroutine
def gen_based_coro():
    yield from asyncio.sleep(1)
"""


@types.coroutine
def gen_based_coro() -> Generator[None]:
    yield from asyncio.sleep(1)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Now it works with @types.coroutine only
@types.coroutine
def yield_from_task_example() -> Generator[None]:
    # create a task to sleep for 5 seconds
    task = asyncio.create_task(asyncio.sleep(1))
    yield from task


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
@asyncio.coroutine
def go_to_sleep(sleep):
    print(f"sleeping for {sleep} seconds in thread {current_thread().name}")
    yield from asyncio.sleep(sleep)
"""


@types.coroutine
def go_to_sleep_yield_from(sleep: int) -> Generator[None]:
    print(f"sleeping for {sleep} seconds in thread {current_thread().name}")
    yield from asyncio.sleep(sleep)


async def go_to_sleep(sleep: int) -> None:
    print(f"sleeping for {sleep} seconds in thread {current_thread().name}")
    time.sleep(sleep)  # sync, sleeps sum(sleep) across calls
    # await asyncio.sleep(sleep)  # async, sleeps max(sleep) across calls


"""
@asyncio.coroutine
def do_something_important(sleep):
    yield from go_to_sleep(sleep)
"""


@types.coroutine
def do_something_important_yield_from(sleep: int) -> Generator[None]:
    yield from go_to_sleep(sleep)


async def do_something_important(sleep: int) -> None:
    await go_to_sleep_yield_from(sleep)


def main() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        # 1st example
        """
        gen = coro()

        # `hello_routine` is an iterable, generator and a generator-based coroutine
        print(isinstance(hello_routine(), types.GeneratorType))
        print(isinstance(hello_routine(), Iterable))
        print(isinstance(hello_routine(), Generator))

        # in fact, coro which yields from `hello_routine` is also an iterable and a generator based coroutine
        print(isinstance(gen, types.GeneratorType))
        print(isinstance(gen, Iterable))
        print(isinstance(gen, Generator))

        for _ in gen:
            pass
        """

        print("Running gen_based_coro")
        gen = gen_based_coro()
        loop.run_until_complete(gen)

        f: asyncio.Future[str] = loop.create_future()
        it = iter(f)  # Future has an __iter__() method
        print(next(it))
        f.set_result("hello")  # set the future's result and mark it done
        try:
            next(it)
        except StopIteration as si:
            print(f"Caught {si.value}")

        # 4th example
        print("Running yield_from_task_example")
        loop.run_until_complete(yield_from_task_example())

        # 5th example
        now = time.time()
        loop.run_until_complete(
            asyncio.gather(
                do_something_important(3),
                do_something_important_yield_from(2),
            )
        )
        end = time.time()
        print(f"total time to run the script: {end - now}")

    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == "__main__":
    main()

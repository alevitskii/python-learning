import asyncio
import random
from collections.abc import AsyncGenerator


async def coroutine() -> int:
    await asyncio.sleep(0.1)
    return random.randint(1, 10000)


async def record_streamer(max_rows: int) -> AsyncGenerator[tuple[int, int]]:
    current_row = 0
    while current_row < max_rows:
        row = (current_row, await coroutine())
        current_row += 1
        yield row


async def main() -> None:
    print([i async for i in record_streamer(max_rows=5)])


if __name__ == "__main__":
    asyncio.run(main())

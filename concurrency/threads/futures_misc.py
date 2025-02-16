import time
from concurrent.futures import (
    Future,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
    wait,
)


def square(item: int) -> int:
    if item != 1:
        time.sleep(4)

    return item * item


def main() -> None:
    # 1st example
    lst: list[Future[int]] = []
    threadExecutor = ThreadPoolExecutor(max_workers=10)
    processExecutor = ProcessPoolExecutor(max_workers=10)

    for i in range(1, 6):
        lst.append(threadExecutor.submit(square, i))

    for i in range(6, 11):
        lst.append(processExecutor.submit(square, i))

    result = wait(lst, timeout=0.01, return_when="FIRST_COMPLETED")
    print(
        f"completed futures count: {len(result.done)} and uncompleted futures count: {len(result.not_done)}\n"
    )

    threadExecutor.shutdown()
    processExecutor.shutdown()

    # 2nd example
    lst2: list[Future[int]] = []
    processExecutor = ProcessPoolExecutor(max_workers=10)

    for i in range(1, 6):
        lst2.append(processExecutor.submit(square, i))

    result2 = as_completed(lst2, timeout=1)

    for ftr in result2:
        print(ftr.result())

    processExecutor.shutdown()


if __name__ == "__main__":
    main()

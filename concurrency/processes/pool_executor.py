import multiprocessing as mp
import os
from concurrent.futures import Future, ProcessPoolExecutor
from threading import current_thread


def say_hi(item: str) -> None:
    print(
        f"\nhi {item} executed in thread id {current_thread().name} in process id {os.getpid()} "
        f"with name {mp.current_process().name}",
        flush=True,
    )


def main() -> None:
    print(f"Main process id {os.getpid()}")
    mp.set_start_method("spawn")

    lst: list[Future[None]] = []
    with ProcessPoolExecutor(max_workers=10) as executor:
        for i in range(1, 10):
            lst.append(executor.submit(say_hi, f"guest{i}"))

        for future in lst:
            future.result()

    # lst: list[Future[None]] = []
    # executor = ProcessPoolExecutor(max_workers=10)
    # for i in range(1, 10):
    #     lst.append(executor.submit(say_hi, f"guest{i}"))

    # for future in lst:
    #     future.result()

    # executor.shutdown()


if __name__ == "__main__":
    main()

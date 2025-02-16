from concurrent.futures import Future, ThreadPoolExecutor
from multiprocessing import cpu_count
from threading import Thread, current_thread
from time import sleep


def say_hi(item: str) -> None:
    print(f"\nhi {item} executed in thread id {current_thread().name}", flush=True)


def say_hi2() -> None:
    sleep(1)
    print(f"\nhi executed in thread id {current_thread().name}", flush=True)


def main() -> None:
    print(cpu_count())
    lst: list[Thread] = []
    for i in range(1, 10):
        t = Thread(target=say_hi2, name=f"Worker-{i:03d}")
        t.start()
        lst.append(t)
    for tt in lst:
        tt.join()

    fut_list: list[Future[None]] = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(1, 10):
            fut_list.append(executor.submit(say_hi, f"guest{i}"))

        for future in fut_list:
            future.result()

    executor = ThreadPoolExecutor(max_workers=10)
    fut_list.clear()
    for i in range(1, 10):
        fut_list.append(executor.submit(say_hi, f"guest{i}"))

    for future in fut_list:
        future.result()

    executor.shutdown()


if __name__ == "__main__":
    main()

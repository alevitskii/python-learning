import random
import time
from threading import Barrier, Thread, current_thread


def thread_task(barrier: Barrier) -> None:
    time.sleep(random.randint(0, 5))
    print(f"\nCurrently {barrier.n_waiting} threads blocked on barrier")
    barrier.wait()


def when_all_threads_released() -> None:
    print(f"All threads released, reported by {current_thread().name}")


def main() -> None:
    num_threads = 5
    barrier = Barrier(num_threads, action=when_all_threads_released)
    threads: list[Thread] = []

    for _ in range(num_threads):
        threads.append(Thread(target=thread_task, args=(barrier,)))

    for t in threads:
        t.start()


if __name__ == "__main__":
    main()

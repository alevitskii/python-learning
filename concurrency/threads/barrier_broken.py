import time
from threading import Barrier, Thread


def thread_task(barrier: Barrier) -> None:
    print(f"\nCurrently {barrier.n_waiting} threads blocked on barrier")
    barrier.wait()
    print("Barrier broken")


def main() -> None:
    num_threads = 5
    barrier = Barrier(num_threads + 1)
    threads: list[Thread] = []

    for _ in range(num_threads):
        threads.append(Thread(target=thread_task, args=(barrier,)))

    for t in threads:
        t.start()

    time.sleep(3)

    print("Main thread about to invoke abort on barrier")
    barrier.abort()


if __name__ == "__main__":
    main()

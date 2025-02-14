import multiprocessing as mp
import random
import time
from multiprocessing.synchronize import Barrier


def process_task(barrier: Barrier) -> None:
    time.sleep(random.randint(0, 5))
    print(f"\nCurrently {barrier.n_waiting} processes blocked on barrier", flush=True)
    barrier.wait()


def when_all_processes_released() -> None:
    print(
        f"\nAll processes released, reported by {mp.current_process().name}", flush=True
    )


def main() -> None:
    num_processes = 5
    barrier = mp.Barrier(num_processes, action=when_all_processes_released)
    processes: list[mp.Process] = []

    for _ in range(num_processes):
        processes.append(mp.Process(target=process_task, args=(barrier,)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()

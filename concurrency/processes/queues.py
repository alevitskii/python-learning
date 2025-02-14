from __future__ import annotations

import multiprocessing as mp
import queue
import random


def child_process(q: mp.Queue[int]) -> None:
    count = 0
    while not q.empty():
        try:
            # default get is blocking so one of the processes may be blocked
            # when both get True for "not q.empty()" check with only 1 element
            # left in the queue
            print(q.get(block=False))
            count += 1
        except queue.Empty:
            pass

    print(
        f"child process {mp.current_process().name} processed {count} items from the queue",
        flush=True,
    )


def main() -> None:
    q: mp.Queue[int] = mp.Queue()

    print(f"This machine has {mp.cpu_count()} CPUs")
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = mp.Process(target=child_process, args=(q,))
    p2 = mp.Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()

from __future__ import annotations

import multiprocessing as mp
import random
import time
from multiprocessing.synchronize import Lock


def child_process(q: mp.Queue[int], lock: Lock) -> None:
    count = 0
    keep_going = True

    while keep_going:
        lock.acquire()
        if not q.empty():
            print(q.get())
            count += 1
        else:
            keep_going = False
        lock.release()
        # Added this sleep so that not all items get processed by
        # a single process
        time.sleep(0.001)

    print(
        f"child process {mp.current_process().name} processed {count} items from the queue",
        flush=True,
    )


def main() -> None:
    print(f"This machine has {mp.cpu_count()} CPUs")
    lock = mp.Lock()
    q: mp.Queue[int] = mp.Queue()

    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = mp.Process(target=child_process, args=(q, lock))
    p2 = mp.Process(target=child_process, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()

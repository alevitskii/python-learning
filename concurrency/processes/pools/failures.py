from __future__ import annotations

import multiprocessing as mp
import os
import random

random.seed()


def square(arg: int) -> int | None:
    i = random.randrange(0, 5)
    try:
        if i % 5 == 0:
            print("injecting failure", flush=True)
            raise Exception("Failure!!!")
        return arg * arg
    except Exception:
        getattr(square, "q").put(arg)
    return None


def init(main_id: int, q: mp.Queue[int]) -> None:
    print(
        f"pool process with id {os.getpid()} received a task from main process with id {main_id}",
        flush=True,
    )
    setattr(square, "q", q)


def queue_to_list(q: mp.Queue[int]) -> tuple[list[int], int]:
    lst = []
    while not q.empty():
        lst.append(q.get())

    return lst, len(lst)


def main() -> None:
    q: mp.Queue[int] = mp.Queue()
    failures = 0
    done = False
    lst = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    pool = mp.Pool(
        processes=5, initializer=init, initargs=(os.getpid(), q), maxtasksperchild=50
    )

    final_results: list[list[int | None]] = []
    while not done:
        res = pool.map(square, lst, chunksize=2)
        final_results.append(res)

        if not q.empty():
            # retrying
            lst, i = queue_to_list(q)
            failures += i
        else:
            done = True

    print(f"failures: {failures}")
    print("final results", final_results)


if __name__ == "__main__":
    main()

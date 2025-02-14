from __future__ import annotations

import ctypes
import multiprocessing as mp
from multiprocessing.sharedctypes import Synchronized, SynchronizedArray
from multiprocessing.synchronize import Semaphore


def child_process(
    sem1: Semaphore,
    sem2: Semaphore,
    arr: SynchronizedArray[int],
    var: Synchronized[int],
) -> None:
    print(
        f"Child process received arr = {arr[0]} with id {id(arr)} from queue",
        flush=True,
    )
    print(
        f"Child process received var = {var.value} with id {id(var)} from queue",
        flush=True,
    )
    sem1.release()
    sem2.acquire()

    print(
        f"After changes by parent process, child process sees arr as = {arr[0]}",
        flush=True,
    )
    print(
        f"After changes by parent process, child process sees var as = {var.value}",
        flush=True,
    )


def main() -> None:
    sem1 = mp.Semaphore(0)
    sem2 = mp.Semaphore(0)
    print(f"This machine has {mp.cpu_count()} CPUs")

    arr = mp.Array(ctypes.c_int, range(5))
    var = mp.Value(ctypes.c_uint, 1)
    print(f"Parent process puts item on queue with ids {id(arr)}, {id(var)}")

    process = mp.Process(target=child_process, args=(sem1, sem2, arr, var))
    process.start()

    sem1.acquire()

    # change var and verify the change is reflected in the child process
    arr[0] += 100
    var.value += 2
    print(
        f"Parent process changed the enqueued item to {arr[0]}, {var.value}",
        flush=True,
    )
    sem2.release()
    process.join()


if __name__ == "__main__":
    main()

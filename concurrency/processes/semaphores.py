from __future__ import annotations

import multiprocessing as mp
import time
from ctypes import c_bool
from multiprocessing.sharedctypes import Synchronized
from multiprocessing.synchronize import Semaphore


def process_A(sem1: Semaphore, sem2: Semaphore, exit: Synchronized[bool]) -> None:
    while not exit.value:
        print("ping", flush=True)
        sem1.release()
        sem2.acquire()
        time.sleep(0.05)


def process_B(sem1: Semaphore, sem2: Semaphore, exit: Synchronized[bool]) -> None:
    while not exit.value:
        # wait for a prime number to become available
        sem1.acquire()
        print("pong", flush=True)
        sem2.release()
        time.sleep(0.05)


def main() -> None:
    sem1 = mp.Semaphore(0)
    sem2 = mp.Semaphore(0)

    exit_prog = mp.Value(c_bool, False)

    processA = mp.Process(target=process_A, args=(sem1, sem2, exit_prog))
    processA.start()

    processB = mp.Process(target=process_B, args=(sem1, sem2, exit_prog))
    processB.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog.value = True

    processA.join()
    processB.join()


if __name__ == "__main__":
    main()

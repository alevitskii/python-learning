from __future__ import annotations

import ctypes
import multiprocessing as mp
import time
from multiprocessing.sharedctypes import Synchronized
from multiprocessing.synchronize import Condition


def printer_process(
    exit_prog: Synchronized[bool],
    found_prime: Synchronized[bool],
    prime: Synchronized[int],
    cond_var: Condition,
) -> None:
    while not exit_prog.value:
        cond_var.acquire()
        while not found_prime.value and not exit_prog.value:
            cond_var.wait()
        cond_var.release()

        if not exit_prog.value:
            print(prime.value)
            prime.value = 0

            cond_var.acquire()
            found_prime.value = False
            cond_var.notify()
            cond_var.release()


def is_prime(num: int) -> bool:
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_process(
    exit_prog: Synchronized[bool],
    found_prime: Synchronized[bool],
    prime: Synchronized[int],
    cond_var: Condition,
) -> None:
    i = 1

    while not exit_prog.value:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(0.01)

        prime.value = i

        cond_var.acquire()
        found_prime.value = True
        cond_var.notify()
        cond_var.release()
        # probably, `release` above and `acquire` below could be removed
        cond_var.acquire()
        while found_prime.value and not exit_prog.value:
            cond_var.wait()
        cond_var.release()

        i += 1


def main() -> None:
    cond_var = mp.Condition()
    prime = mp.Value(ctypes.c_int, 0)
    found_prime = mp.Value(ctypes.c_bool, False)
    exit_prog = mp.Value(ctypes.c_bool, False)

    printerProcess = mp.Process(
        target=printer_process, args=(exit_prog, found_prime, prime, cond_var)
    )
    printerProcess.start()

    finderProcess = mp.Process(
        target=finder_process, args=(exit_prog, found_prime, prime, cond_var)
    )
    finderProcess.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog.value = True

    # Let the threads exit
    cond_var.acquire()
    cond_var.notify_all()
    cond_var.release()

    printerProcess.join()
    finderProcess.join()


if __name__ == "__main__":
    main()

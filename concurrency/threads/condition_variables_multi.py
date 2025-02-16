import time
from threading import Condition, Thread, current_thread


def printer_thread_func(
    cond_var: Condition,
    exit_prog: list[bool],
    prime_holder: list[int | None],
    found_prime: list[bool],
) -> None:
    while not exit_prog[0]:
        cond_var.acquire()
        while not found_prime[0] and not exit_prog[0]:
            cond_var.wait()

        if not exit_prog[0]:
            print(f"{current_thread().name} prints {prime_holder}")

            prime_holder[0] = None

            found_prime[0] = False
            cond_var.notifyAll()
        cond_var.release()

    print(f"printer {current_thread().name} exiting")


def is_prime(num: int) -> bool:
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_thread_func(
    cond_var: Condition,
    exit_prog: list[bool],
    prime_holder: list[int | None],
    found_prime: list[bool],
) -> None:
    i = 1

    while not exit_prog[0]:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(0.01)

        prime_holder[0] = i

        cond_var.acquire()
        found_prime[0] = True
        cond_var.notify()
        cond_var.release()

        cond_var.acquire()
        while found_prime[0] and not exit_prog[0]:
            cond_var.wait()
        cond_var.release()

        i += 1

    print("finder exiting")


def main() -> None:
    cond_var = Condition()
    found_prime = [False]
    prime_holder = [None]
    exit_prog = [False]

    printerThread = Thread(
        target=printer_thread_func,
        args=(cond_var, exit_prog, prime_holder, found_prime),
    )
    printerThread.start()

    printerThread2 = Thread(
        target=printer_thread_func,
        args=(cond_var, exit_prog, prime_holder, found_prime),
    )
    printerThread2.start()

    printerThread3 = Thread(
        target=printer_thread_func,
        args=(cond_var, exit_prog, prime_holder, found_prime),
    )
    printerThread3.start()

    finderThread = Thread(
        target=finder_thread_func, args=(cond_var, exit_prog, prime_holder, found_prime)
    )
    finderThread.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    # Let the threads exit
    exit_prog[0] = True

    cond_var.acquire()
    cond_var.notify_all()
    cond_var.release()

    printerThread.join()
    printerThread2.join()
    printerThread3.join()
    finderThread.join()


if __name__ == "__main__":
    main()

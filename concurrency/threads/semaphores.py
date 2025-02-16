import time
from threading import Semaphore, Thread


def printer_thread(
    sem_find: Semaphore,
    sem_print: Semaphore,
    prime_holder: list[int | None],
    exit_prog: list[bool],
) -> None:
    while not exit_prog[0]:
        # wait for a prime number to become available
        sem_find.acquire()

        # print the prime number
        print(prime_holder[0])
        prime_holder[0] = None

        # let the finder thread find the next prime
        sem_print.release()


def is_prime(num: int) -> bool:
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True


def finder_thread(
    sem_find: Semaphore,
    sem_print: Semaphore,
    prime_holder: list[int],
    exit_prog: list[bool],
) -> None:
    i = 1

    while not exit_prog[0]:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread so that we can see the output
            time.sleep(0.01)

        prime_holder[0] = i

        # let the printer thread know we have a prime available for printing
        sem_find.release()

        # wait for printer thread to complete printing the prime number
        sem_print.acquire()

        i += 1


def main() -> None:
    sem_find = Semaphore(0)
    sem_print = Semaphore(0)
    prime_holder = [None]
    exit_prog = [False]

    printerThread = Thread(
        target=printer_thread, args=(sem_find, sem_print, prime_holder, exit_prog)
    )
    printerThread.start()

    finderThread = Thread(
        target=finder_thread, args=(sem_find, sem_print, prime_holder, exit_prog)
    )
    finderThread.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog[0] = True

    printerThread.join()
    finderThread.join()


if __name__ == "__main__":
    main()

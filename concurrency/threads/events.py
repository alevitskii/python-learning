import time
from threading import Event, Thread


def printer_thread(
    prime_available: Event,
    prime_printed: Event,
    prime_holder: list[int | None],
    exit_prog: list[bool],
) -> None:
    while not exit_prog[0]:
        # wait for a prime number to become available
        prime_available.wait()

        # print the prime number
        print(prime_holder[0])
        prime_holder[0] = None

        # reset the event to false
        prime_available.clear()

        # let the finder thread know that printing is done
        prime_printed.set()


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
    prime_available: Event,
    prime_printed: Event,
    prime_holder: list[int | None],
    exit_prog: list[bool],
) -> None:
    i = 1

    while not exit_prog[0]:
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(0.01)

        prime_holder[0] = i

        # let the printer thread know we have
        # a prime available for printing
        prime_available.set()

        # wait for printer thread to print the prime
        prime_printed.wait()

        # reset the flag
        prime_printed.clear()

        i += 1


def main() -> None:
    prime_available = Event()
    prime_printed = Event()
    prime_holder = [None]
    exit_prog = [False]

    printerThread = Thread(
        target=printer_thread,
        args=(prime_available, prime_printed, prime_holder, exit_prog),
    )
    printerThread.start()

    finderThread = Thread(
        target=finder_thread,
        args=(prime_available, prime_printed, prime_holder, exit_prog),
    )
    finderThread.start()

    # Let the threads run for 3 seconds
    time.sleep(3)

    exit_prog[0] = True
    prime_available.set()
    prime_printed.set()

    printerThread.join()
    finderThread.join()


if __name__ == "__main__":
    main()

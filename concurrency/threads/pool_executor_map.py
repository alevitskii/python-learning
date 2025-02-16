import time
from concurrent.futures import ThreadPoolExecutor


def square(item: int) -> int:
    if item == 5:
        time.sleep(10)
    return item * item


def main() -> None:
    with ThreadPoolExecutor(max_workers=10) as executor:
        it = executor.map(
            square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=1, timeout=2
        )
        for sq in it:
            print(sq)

    # executor = ThreadPoolExecutor(max_workers=10)

    # it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=1, timeout=2)

    # for sq in it:
    #     print(sq)

    # executor.shutdown()


if __name__ == "__main__":
    main()

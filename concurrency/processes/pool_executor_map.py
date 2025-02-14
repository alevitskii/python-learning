import os
from concurrent.futures import ProcessPoolExecutor


def square(item: int) -> int:
    print(f"Executed in process with id {os.getpid()}, item {item}", flush=True)
    return item * item


def main() -> None:
    with ProcessPoolExecutor(max_workers=10) as executor:
        it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=1)
        for sq in it:
            print(sq)

    # executor = ProcessPoolExecutor(max_workers=10)
    # it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=1)
    # for sq in it:
    #     print(sq)
    # executor.shutdown()


if __name__ == "__main__":
    main()

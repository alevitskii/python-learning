import multiprocessing as mp
import os


def square(arg: int) -> int:
    return arg * arg


def init(main_id: int) -> None:
    print(
        f"pool process with id {os.getpid()} received a task from main process with id {main_id}",
        flush=True,
    )


def main() -> None:
    pool = mp.Pool(
        processes=5, initializer=init, initargs=(os.getpid(),), maxtasksperchild=50
    )

    res = pool.imap_unordered(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=2)

    for sq in res:
        print(sq)


if __name__ == "__main__":
    main()

import os
from multiprocessing import Pool


def square(arg1: int, arg2: str) -> str:
    return f"{arg2}-{arg1 * arg1}"


def init(main_id: int) -> None:
    print(
        f"pool process with id {os.getpid()} received a task from main process with id {main_id}",
        flush=True,
    )


def on_success(new_result: list[str]) -> None:
    for x in new_result:
        print(f"\n{x}")


def on_error(err: BaseException) -> None:
    print(f"Error : {err}")


def main() -> None:
    pool = Pool(
        processes=5, initializer=init, initargs=(os.getpid(),), maxtasksperchild=50
    )

    _ = pool.starmap_async(
        square,
        ((1, "chunk1"), (3, "chunk2"), (5, "chunk3"), (7, "chunk4"), (9, "chunk5")),
        chunksize=2,
        callback=on_success,
        error_callback=on_error,
    )

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()

import os
from multiprocessing import Pool


def square(arg: int) -> int:
    return arg * arg


def init(main_id: int) -> None:
    print(
        f"pool process with id {os.getpid()} received a task from main process with id {main_id}",
        flush=True,
    )


def on_success(new_result: list[int]) -> None:
    print(f"\nReceived result as: {new_result}")


def on_error(err: BaseException) -> None:
    print(f"Error : {err}")


def main() -> None:
    pool = Pool(
        processes=5, initializer=init, initargs=(os.getpid(),), maxtasksperchild=50
    )

    _ = pool.map_async(
        square,
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        chunksize=2,
        callback=on_success,
        error_callback=on_error,
    )
    # res = pool.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=2)
    # print(res)

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()

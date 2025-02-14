import multiprocessing as mp
import os
import time


def init(main_id: int) -> None:
    # this message is printed twice when maxtasksperchild is set to 1
    print(
        f"pool process with id {os.getpid()} received a task from main process with id {main_id}"
    )


def square(x: int) -> int:
    return x * x


def on_success(result: int) -> None:
    print(f"result is {result}")


def on_error(err: BaseException) -> None:
    print(f"error is {err}")


def main() -> None:
    main_process_id = os.getpid()

    pool = mp.Pool(
        processes=1, initializer=init, initargs=(main_process_id,), maxtasksperchild=1
    )

    result = pool.apply_async(
        square, (9,), callback=on_success, error_callback=on_error
    )
    print(result)

    # prevent main from exiting before the pool process completes
    time.sleep(6)


if __name__ == "__main__":
    main()

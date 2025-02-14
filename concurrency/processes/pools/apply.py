import multiprocessing as mp
import os


def init(main_id: int) -> None:
    print(
        f"pool process with id {os.getpid()} received a task from main process with id {main_id}"
    )


def square(x: int) -> int:
    return x * x


def main() -> None:
    main_process_id = os.getpid()

    pool = mp.Pool(
        processes=1, initializer=init, initargs=(main_process_id,), maxtasksperchild=1
    )

    result = pool.apply(square, (3,))
    print(result)


if __name__ == "__main__":
    main()

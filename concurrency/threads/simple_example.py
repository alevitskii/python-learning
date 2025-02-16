from threading import Thread, current_thread


def thread_task(a: int, b: int, c: int, *, key1: int, key2: int) -> None:
    print(f"{current_thread().name} received the arguments: {a} {b} {c} {key1} {key2}")


def main() -> None:
    myThread = Thread(
        group=None,  # reserved
        target=thread_task,  # callable object
        name="demoThread",  # name of thread
        args=(1, 2, 3),  # arguments passed to the target
        kwargs={"key1": 777, "key2": 111},  # dictionary of keyword arguments
        daemon=None,  # set true to make the thread a daemon
    )
    myThread.start()  # start the thread
    myThread.join()  # wait for the thread to complete


if __name__ == "__main__":
    main()

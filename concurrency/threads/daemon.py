import time
from threading import Thread, current_thread


def regular_thread_task() -> None:
    while True:
        print(f"{current_thread().name} executing")
        time.sleep(1)


def daemon_thread_task() -> None:
    # while True:
    print(f"{current_thread().name} executing")
    time.sleep(1)
    print(f"{current_thread().name} executing 2")


def main() -> None:
    regularThread = Thread(
        target=regular_thread_task, name="regularThread", daemon=False
    )
    regularThread.start()  # start the regular thread
    time.sleep(3)
    print("Main thread exiting but Python program doesn't")

    # daemonThread = Thread(target=daemon_thread_task, name="daemonThread", daemon=True)
    # daemonThread.start()  # start the daemon thread
    # # daemonThread.join()
    # # time.sleep(3)
    # print("Main thread exiting and Python program too")


if __name__ == "__main__":
    main()

from threading import RLock, Thread


def child_task(rlock: RLock) -> None:
    rlock.acquire()
    print("child task executing")
    rlock.release()


def perform_unlock(rlock: RLock) -> None:
    rlock.release()
    print("child task executing")
    rlock.release()


def main() -> None:
    rlock = RLock()
    rlock.acquire()
    rlock.acquire()
    rlock.release()
    # With the line below commented out the program will hang.
    rlock.release()
    thread = Thread(target=child_task, args=(rlock,))
    thread.start()
    thread.join()

    # # reentrant lock acquired by main thread
    # rlock.acquire()
    # # let's attempt to unlock using a child thread (RuntimeError: cannot release un-acquired lock)
    # thread = Thread(target=perform_unlock, args=(rlock,))
    # thread.start()
    # thread.join()


if __name__ == "__main__":
    main()

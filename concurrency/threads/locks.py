import time
from threading import Lock, Thread, current_thread


def thread1_operations(lock: Lock, shared_state: list[int]) -> None:
    lock.acquire()
    print(f"{current_thread().name} has acquired the lock")

    time.sleep(3)
    shared_state[0] = 777

    print(f"{current_thread().name} about to release the lock")
    lock.release()
    print(f"{current_thread().name} released the lock")


def thread2_operations(lock: Lock, shared_state: list[int]) -> None:
    print(f"{current_thread().name} is attempting to acquire the lock")
    lock.acquire()
    print(f"{current_thread().name} has acquired the lock")

    print(shared_state[0])
    print(f"{current_thread().name} about to release the lock")
    lock.release()
    print(f"{current_thread().name} released the lock")


def main() -> None:
    shared_state = [1, 2, 3]
    lock = Lock()
    # create and run the two threads
    thread1 = Thread(
        target=thread1_operations, args=(lock, shared_state), name="thread1"
    )
    thread1.start()

    thread2 = Thread(
        target=thread2_operations, args=(lock, shared_state), name="thread2"
    )
    thread2.start()

    # wait for the two threads to complete
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()

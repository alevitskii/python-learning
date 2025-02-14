import multiprocessing as mp
import time
from multiprocessing.synchronize import RLock


def child_task(rlock: RLock) -> None:
    n = 5
    for _ in range(n):
        rlock.acquire()
        print(f"I am child process {mp.current_process().name}")
        time.sleep(0.01)

    for _ in range(n):
        rlock.release()


def main() -> None:
    rlock = mp.RLock()
    rlock.acquire()

    process1 = mp.Process(target=child_task, args=(rlock,))
    process1.start()

    process2 = mp.Process(target=child_task, args=(rlock,))
    process2.start()

    # sleep 3 seconds before releasing the lock
    time.sleep(3)
    rlock.release()

    process1.join()
    process2.join()


if __name__ == "__main__":
    main()

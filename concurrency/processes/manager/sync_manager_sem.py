import time
from multiprocessing import Process
from multiprocessing.managers import SyncManager
from threading import Semaphore

# port number on which the manager runs and another can connect at
port_num = 55555


def return_my_string() -> str:
    return "my string test"


def process_task(sem: Semaphore) -> None:
    manager = SyncManager(address=("127.0.0.1", port_num))
    manager.register("get_my_string")
    manager.connect()
    proxy = manager.get_my_string()  # type: ignore

    print(repr(proxy))
    print(str(proxy))
    print("child process exiting in 5 seconds")

    time.sleep(5)
    sem._callmethod("release")  # type: ignore

    # invoking methods on the proxy's referent
    print(proxy._callmethod("isdigit"))
    print(proxy._callmethod("capitalize"))


if __name__ == "__main__":
    manager = SyncManager(address=("127.0.0.1", port_num))

    # Register our type
    # Can't use lambda as callable because lambda is not pickable.
    # When use fork to create a process everything should work fine but Windows doesn't support fork.
    manager.register("get_my_string", callable=return_my_string)
    manager.start()

    # get a proxy for a Semaphore
    sem = manager.Semaphore(0)

    # pass the semahore to the other process
    p = Process(target=process_task, args=(sem,))
    p.start()

    # wait for the semaphore to be set
    sem._callmethod("acquire")  # type: ignore

    print("Main process exiting")

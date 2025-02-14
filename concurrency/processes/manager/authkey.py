import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

# port number on which the manager runs and another can connect at
port_num = 55555


def return_my_string() -> str:
    return "my string test"


def process_task() -> None:
    manager = BaseManager(address=("127.0.0.1", port_num), authkey=b"MySecretKey")
    manager.register("get_my_string")
    manager.connect()
    proxy = manager.get_my_string()  # type: ignore

    print(repr(proxy))
    print(str(proxy))

    print(proxy.isdigit())
    print(proxy.capitalize())


if __name__ == "__main__":
    manager = BaseManager(address=("127.0.0.1", port_num), authkey=b"MySecretKey")

    # Register our type
    manager.register("get_my_string", callable=return_my_string)
    manager.start()

    p = Process(target=process_task)
    p.start()

    time.sleep(3)
    print("Exiting main process")
    manager.shutdown()

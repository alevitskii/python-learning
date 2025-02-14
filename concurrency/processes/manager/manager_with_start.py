import random
import time
from multiprocessing import Manager, Process, current_process
from multiprocessing.managers import BaseManager, ListProxy


def top_level_function() -> ListProxy[str]:
    return (Manager()).list([f"set by {current_process().name}"])


def ProcessA(port_num: int) -> None:
    manager = BaseManager(address=("127.0.0.1", port_num))
    manager.register("get_my_items", callable=top_level_function, proxytype=ListProxy)
    manager.start()

    time.sleep(3)


def ProcessB(port_num: int) -> None:
    manager = BaseManager(address=("127.0.0.1", port_num))

    manager.register("get_my_items")
    manager.connect()
    proxy_items = manager.get_my_items()  # type: ignore
    proxy_items.append(f"set by {current_process().name}")

    print(list(proxy_items))


def main() -> None:
    port_num = random.randint(10000, 60000)

    # Start another process which will access the shared string
    p1 = Process(target=ProcessA, args=(port_num,))
    p1.start()

    time.sleep(0.8)

    p2 = Process(target=ProcessB, args=(port_num,))
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()

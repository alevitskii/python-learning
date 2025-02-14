import random
import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager, Server
from threading import Thread


def ProcessA(port_num: int) -> None:
    my_string = "hello, World!"
    manager = BaseManager(address=("127.0.0.1", port_num))
    manager.register("get_my_string", callable=lambda: my_string)
    server = manager.get_server()

    Thread(target=shutdown, args=(server,)).start()

    server.serve_forever()


def ProcessB(port_num: int) -> None:
    manager = BaseManager(address=("127.0.0.1", port_num))
    manager.register("get_my_string")
    manager.connect()
    proxy_my_string = manager.get_my_string()  # type: ignore

    print(f"In ProcessB repr(proxy_my_string) = {proxy_my_string!r}")
    print(f"In ProcessB str(proxy_my_string) = {proxy_my_string}")

    print(proxy_my_string)
    print(proxy_my_string.capitalize())
    print(proxy_my_string._callmethod("capitalize"))


def shutdown(server: Server) -> None:
    time.sleep(3)
    server.stop_event.set()  # type: ignore


def main() -> None:
    port_num = random.randint(10000, 60000)

    # Start another process which will access the shared string
    p1 = Process(target=ProcessA, args=(port_num,), name="ProcessA")
    p1.start()

    time.sleep(1)

    p2 = Process(target=ProcessB, args=(port_num,), name="ProcessB")
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()

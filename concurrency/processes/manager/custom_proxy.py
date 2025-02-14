from __future__ import annotations

import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager, BaseProxy

port_num = 55555


def make_pair() -> Pair:
    return Pair(0, 0)


class MyProxy(BaseProxy):
    @property
    def x(self) -> int:
        # we could also have method getter and setters in Pair so we don't have to create get/set
        return self._callmethod("get", "x")  # type: ignore

    @x.setter
    def x(self, value: int) -> None:
        # we could also have method getter and setters in
        self._callmethod("set", ("x", value))


def process_task() -> None:
    manager = BaseManager(address=("127.0.0.1", port_num))
    manager.register("Pair", proxytype=MyProxy)
    # This will cause an error
    # manager.register("Pair", proxytype=MyProxy, create_method=False)
    manager.connect()

    p = manager.Pair()  # type: ignore
    print(p.x)
    p.x = 5
    print(p.x)


class Pair:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get(self, name: str) -> object:
        return getattr(self, name)

    def set(self, name: str, value: object) -> None:
        setattr(self, name, value)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y


def main() -> None:
    p1 = Process(target=process_task)
    manager = BaseManager(address=("127.0.0.1", port_num))

    # If you wanted to set create_method=False while forking the process you would have to do it here too.
    # Can't use lambda because it's not pickable (when "spawn" method to create processes is used, with "fork" works fine).
    manager.register(
        "Pair", callable=make_pair, exposed=["get", "set"], create_method=False
    )

    manager.start()
    p1.start()
    time.sleep(3)
    manager.shutdown()


if __name__ == "__main__":
    main()

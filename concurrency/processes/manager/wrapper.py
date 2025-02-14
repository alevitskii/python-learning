from __future__ import annotations

import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

port_num = 55555


class ItemWrapper[T]:
    def __init__(self, res: Item) -> None:
        self.item = res

    def set_wrapped_item(self, value: str) -> None:
        self.item.change(value)

    def get_wrapped_item(self) -> str:
        return self.item.retrieve()


class Item:
    def __init__(self, item: str = "initialized") -> None:
        self._item = item

    def change(self, item: str) -> None:
        self._item = item

    def retrieve(self) -> str:
        return self._item


class Pair:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self.i = Item()

    def get_item(self) -> Item:
        return self.i

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y


pair = Pair(15, 6)


def return_pair() -> Pair:
    return pair


def consumer_process() -> None:
    mgr = BaseManager(address=("127.0.0.1", port_num))
    mgr.register("ItemWrapper", ItemWrapper)
    mgr.register("get_pair")
    mgr.connect()

    p = mgr.get_pair()  # type: ignore
    proxy1 = p.get_item()
    print(f"proxy1 sees item as : {proxy1.get_wrapped_item()}")
    old_val = proxy1.get_wrapped_item()
    proxy1._callmethod("set_wrapped_item", (7,))
    print(f"proxy1 changes item from {old_val} to {proxy1.get_wrapped_item()}")

    proxy2 = mgr.get_pair().get_item()  # type: ignore
    print(f"proxy2 sees item as : {proxy2.get_wrapped_item()}")
    old_val = proxy2.get_wrapped_item()
    proxy2.set_wrapped_item(11)
    print(f"proxy2 changes item from {old_val} to {proxy2.get_wrapped_item()}")
    print(f"proxy1 sees item as : {proxy1.get_wrapped_item()}")


def producer_process() -> None:
    manager = BaseManager(address=("127.0.0.1", port_num))

    manager.register("ItemWrapper", ItemWrapper)
    manager.register(
        "get_pair", callable=return_pair, method_to_typeid={"get_item": "ItemWrapper"}
    )

    manager.start()
    time.sleep(3)
    print(
        f"\nAfter changes in consumer process, the producer process sees item as = {pair.get_item().retrieve()}"
    )
    manager.shutdown()


def main() -> None:
    p1 = Process(target=producer_process)
    p2 = Process(target=consumer_process)

    p1.start()
    time.sleep(2)
    p2.start()

    p2.join()
    p1.join()


if __name__ == "__main__":
    main()

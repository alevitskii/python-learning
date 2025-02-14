import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import Namespace, SyncManager


def process1(ns: Namespace) -> None:
    print(f"in process1 '{ns.item}'")
    ns.item = "process1 test"


def process2(ns: Namespace) -> None:
    print(f"in process2 '{ns.item}'")
    ns.item = "process2 test"


def main() -> None:
    multiprocessing.set_start_method("spawn")
    # create a namespace
    manager = SyncManager(address=("127.0.0.1", 55555))
    manager.start()
    shared_vars = manager.Namespace()
    shared_vars.item = "empty"
    # _item won't be visible to other processes
    # _item will create an attribute on the namespace proxy and not on the referent
    shared_vars._item = "_empty"

    # create the first process
    p1 = Process(target=process1, args=(shared_vars,))
    p1.start()
    p1.join()

    # create the second process
    p2 = Process(target=process2, args=(shared_vars,))
    p2.start()
    p2.join()

    print(shared_vars.item)


if __name__ == "__main__":
    main()

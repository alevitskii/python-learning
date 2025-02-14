import multiprocessing
from multiprocessing import Process
from multiprocessing.managers import ListProxy, SyncManager

# port number on which the manager runs and another can
# connect at
port_num = 55555


def process1_task(lstProxy: ListProxy[int | list[int]]) -> None:
    lstProxy[0] = 1
    print(f"process 1 sees list as {lstProxy}")
    nested_list: list[int] = [2]
    lstProxy.append(nested_list)

    nested_list.append(99)
    nested_list.append(98)
    nested_list.append(97)
    # doesn't reflect changes to nested_list
    print(f"Child process sees lstProxy as: {lstProxy}")
    lstProxy[3] = nested_list
    # now does
    print(f"Child process sees lstProxy as: {lstProxy}")


def main() -> None:
    multiprocessing.set_start_method("spawn")
    manager = SyncManager(address=("127.0.0.1", port_num))
    manager.start()
    lst = manager.list([0, 0, 0])

    # create first process
    p1 = Process(target=process1_task, args=(lst,))
    p1.start()
    p1.join()


if __name__ == "__main__":
    main()

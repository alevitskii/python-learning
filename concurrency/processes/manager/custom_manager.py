import time
from multiprocessing import Process
from multiprocessing.managers import BaseManager

# port number on which the manager runs and another can connect at
port_num = 55555


class Utility:
    def capitalize(self, name: str) -> str:
        return name.capitalize()


class MyManager(BaseManager):
    pass


MyManager.register("UtilityClass", Utility)


def process_task() -> None:
    my_manager = MyManager(address=("127.0.0.1", port_num))
    my_manager.register("UtilityClass")
    my_manager.connect()

    utility = my_manager.UtilityClass()  # type: ignore
    print(utility.capitalize("hello"))


def main() -> None:
    my_manager = MyManager(address=("127.0.0.1", port_num))

    my_manager.start()
    Process(target=process_task).start()

    time.sleep(3)
    print("Main process exiting")


if __name__ == "__main__":
    main()

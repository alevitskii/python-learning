from threading import Thread, current_thread


class MyTask(Thread):
    def __init__(self) -> None:
        # The two args will not get passed to the overridden run method.
        Thread.__init__(self, name="subclassThread", args=(2, 3))

    def run(self) -> None:
        print(f"{current_thread().name} is executing")


def main() -> None:
    myTask = MyTask()
    myTask.start()  # start the thread
    myTask.join()  # wait for the thread to complete
    print("{0} exiting".format(current_thread().name))


if __name__ == "__main__":
    main()

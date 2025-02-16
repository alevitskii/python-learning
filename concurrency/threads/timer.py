import time
from threading import Timer, current_thread


def say_hi(name: str) -> None:
    print(f"{current_thread().name} says Hi {name}!")


def main() -> None:
    timer = Timer(1, say_hi, args=["reader"])
    timer.start()

    time.sleep(2)

    print(f"{current_thread().name} exiting")


if __name__ == "__main__":
    main()

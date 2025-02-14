import os
from multiprocessing import Process, current_process


def process_task(x: int, y: int, z: int, key1: str, key2: str) -> None:
    print(
        f"\n{current_process().name} has pid: {os.getpid()} with parent pid: {os.getppid()}"
    )
    print(f"Received arguments {x} {y} {z} {key1} {key2}\n")


def main() -> None:
    processes: list[Process] = []

    for i in range(3):
        processes.append(
            Process(
                target=process_task,
                name=f"process-{i}",
                args=(1, 2, 3),
                kwargs={"key1": "arg1", "key2": "arg2"},
            )
        )
        processes[-1].start()

    for process in processes:
        process.join()

    print(f"{current_process().name} has pid: {os.getpid()}")


if __name__ == "__main__":
    main()

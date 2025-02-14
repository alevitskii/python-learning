# Fork isn't available on a Windows platform.
# Fork copies get a memory image identical to the parent's (open file descriptors, locks, data-structures etc).
# Any threads running in the parent process do not exist in the child process.
import multiprocessing
import os
from multiprocessing import Process
from typing import TextIO

file_desc: TextIO | None = None


def process_task() -> None:
    # write to the file in a child process
    if not file_desc:
        raise AssertionError()
    file_desc.write(f"\nline written by child process with id {os.getpid()}")
    file_desc.flush()


if __name__ == "__main__":
    # create a file descriptor in the parent process
    file_desc = open("sample.txt", "w")
    file_desc.write(f"\nline written by parent process with id {os.getpid()}")
    file_desc.flush()

    multiprocessing.set_start_method("fork")

    process = Process(target=process_task)
    process.start()
    process.join()
    file_desc.close()

    # read and print the contents of the file
    file_desc = open("sample.txt", "r")
    print(file_desc.read())

    os.remove("sample.txt")

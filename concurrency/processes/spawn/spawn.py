# Forking produces two processes, whereas exec loads an executable in the existing process's address space.
# The current executable image is replaced with another one loaded from an executable file.
# Spawn is essentially a combination of fork followed by an exec (one of its variants) system call.
# A new python interpreter process is created and the child doesn't inherit any resources
# from the parent process other than those required to execute the specified callable target.
# Multiprocessing uses pickle to transport data between processes.
# This mandates that the arguments being passed to the child process be picklable i.e. they can be serialized.

import multiprocessing as mp

import importing  # noqa: F401

global_arg = "this is a global arg"


def process_task(garg: str, larg: str) -> None:
    print(f"{garg} - {larg}")


def main() -> None:
    # `importing` is reimported in the child process
    mp.set_start_method("spawn")
    local_arg = "this is a local arg"
    process = mp.Process(target=process_task, args=(global_arg, local_arg))
    process.start()
    process.join()
    print("I am parent process")


if __name__ == "__main__":
    main()

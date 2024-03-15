import argparse
import os
import shutil
import sys


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--no-hostenv", dest="hostenv", action="store_false")
    parser.add_argument("--help", action="store_true")
    args, rest = parser.parse_known_args()

    # this is to write both helps
    if args.help:
        parser.print_help()
        width, _ = shutil.get_terminal_size()
        print()
        print("docker run --help:")
        print(width * "=")
        print()
        os.execvp("docker", ("docker", "run", "--help"))

    if args.hostenv:
        cmd = (
            "docker",
            "run",
            "-e",
            f"HOST_USER={os.getuid()}",  # os.getuid, os.getgid are Unix only
            "-e",
            f"HOST_GROUP={os.getgid()}",
            *rest,
        )
    else:
        cmd = ("docker", "run", *rest)
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    main()

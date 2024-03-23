"""
MIT License

Copyright (c) 2021 ArjanCodes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from dataclasses import dataclass


def run_command_v1(command: str) -> None:
    match command:
        case "quit":
            print("Quitting the program.")
        case "reset":
            print("Resetting the system.")
        case other:
            print(f"Unknown command '{other}'.")


def run_command_v2(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading filename {filename}.")
        case ["save", filename]:
            print(f"Saving filename {filename}.")
        case ["quit" | "exit" | "bye", *rest]:
            if "--force" in rest or "-f" in rest:
                print("Sending SIGTERM to all processes and quitting the program.")
            else:
                print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command '{command}'.")


def run_command_v3(command: str) -> None:
    match command.split():
        case ["load", filename] as matched:
            print(f"Loading filename {filename}. Splitted command {matched!r}")
        case ["save", filename]:
            print(f"Saving filename {filename}.")
        case ["quit" | "exit" | "bye", *rest] if "--force" in rest or "-f" in rest:
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case ["quit" | "exit" | "bye"]:
            print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command {command!r}.")


@dataclass
class Command:
    """Class that represents a command."""

    command: str
    arguments: list[str]


def run_command_v4(command: Command) -> None:
    match command:
        case Command(command="load", arguments=[filename]):
            print(f"Loading filename {filename}.")
        case Command(command="save", arguments=[filename]):
            print(f"Saving filename {filename}.")
        case Command(command="quit" | "exit" | "bye", arguments=["--force" | "-f", *_]):
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case Command(command="quit" | "exit" | "bye"):
            print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command {command!r}.")


def main() -> None:
    """Main function."""

    while True:
        command = input("$ ")
        run_command_v3(command)
        # read a command with arguments from the input
        # command, *arguments = shlex.split(input("$ "))

        # run the command
        # run_command_v4(Command(command, arguments))


if __name__ == "__main__":
    main()

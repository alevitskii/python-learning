import shutil
from datetime import datetime


def my_function():
    heading = "Some string"
    width, _ = shutil.get_terminal_size()
    print(f"{heading:=^{width}}")
    print(f"{heading:=>{width}}")
    print(f"{heading:=<{width}}")
    print(heading.center(width, "="))

    integer = -1234567
    print(f"Comma as thousand separators: {integer:,}")

    integer = -1234567
    sep = "_"
    print(f"User's thousand separators: {integer:{sep}}")

    floating_point = 1234567.9876
    print(f"Comma as thousand separators and two decimals: {floating_point:,.2f}")

    date = (10, 6, 2023)
    print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")

    date = datetime(2023, 9, 26)
    print(f"Date: {date:%m/%d/%Y}")

    string = "some string"
    print(f"{string!r}")
    print(f"{string!s}")

    variable = "Some mysterious value"
    # print(f"{variable = }")  # works OK, but IDE highlights
    print(f"{variable=}")


def main() -> None:
    my_function()


if __name__ == "__main__":
    main()

from typing import TypeAlias, TypeGuard

StrCache: TypeAlias = "list[str]"  # a type alias
LOG_PREFIX = "LOG[DEBUG]"  # a module constant


# def is_str_list(val: list[object]) -> bool:
#     """Determines whether all objects in the list are strings"""
#     return all(isinstance(x, str) for x in val)


def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    """Determines whether all objects in the list are strings"""
    return all(isinstance(x, str) for x in val)


def func1(val: list[object]):
    if is_str_list(val):
        print(" ".join(val))  # Error if "-> bool": invalid type


def main() -> None:
    pass


if __name__ == "__main__":
    main()

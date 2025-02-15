# this can be used to define decorators that would work with class methods
from collections.abc import Callable
from functools import wraps
from types import MethodType
from typing import Concatenate, Self, overload


class DBDriver:
    def __init__(self, dbstring: str) -> None:
        self.dbstring = dbstring

    def execute(self, query: str) -> str:
        return f"query {query} at {self.dbstring}"


class inject_db_driver[T]:
    """Convert a string to a DBDriver instance and pass this to the wrapped
    function.
    """

    def __init__(
        self, function: Callable[[Concatenate[T, DBDriver, ...]], str]
    ) -> None:
        self.function = function
        wraps(self.function)(self)

    def __call__(self, dbstring: str) -> str:
        return self.function(DBDriver(dbstring))

    @overload
    def __get__(self, instance: None, owner: type[T]) -> Self: ...

    @overload
    def __get__(self, instance: T, owner: type[T] | None = None) -> T: ...

    def __get__(self, instance: T | None, owner: type[T] = None):
        if instance is None:
            return self
        return self.__class__(MethodType(self.function, instance))


@inject_db_driver
def run_query(driver: DBDriver) -> str:
    return driver.execute("test_function_2")


class DataHandler:
    @inject_db_driver
    def run_query(self, driver: DBDriver) -> str:
        return driver.execute("test_method_2")


class DataHandler2:
    @inject_db_driver
    def run_query(self, driver: DBDriver) -> str:
        return driver.execute("test_method_3")


def main() -> None:
    dh = DataHandler()
    dh2 = DataHandler2()
    print(dh.run_query("test_passes"))
    print(dh2.run_query("test_passes"))
    print(run_query("test_passes"))


if __name__ == "__main__":
    main()

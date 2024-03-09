import functools
from threading import Lock, Thread
from typing import Self, final


# option 1 is to have final decorator to tell that it cannot be sublassed
# and have underscore prefix as a convention (this class shouldn't be instantiated)
# but you have to be careful about adhering to the convention
# also this class is copyable and pickable/unpickable (there hooks to prevent this)
@final
class _Singleton:
    def __init__(self) -> None:
        self.x = 1

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x


# _foo = None
# def get_foo() -> _Singleton:
#     global _foo
#     if _foo is None:
#         _foo = _Singleton()
#     return _foo


@functools.lru_cache(maxsize=1)
def get_foo() -> _Singleton:
    return _Singleton()


# another option is to have a module as a singleton where you define
# functions and variables in global scope
x = 1


def increment_thing(self) -> None:
    global x
    x += 1


def get_thing(self) -> int:
    return x


# another option is to define __new__
@final
class _Singleton2:
    _inst = None
    _inited = False

    def __new__(cls) -> Self:
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __init__(self) -> None:
        # this is to prevent resetting x to 1 on every instantiation
        if type(self)._inited:
            return
        self.x = 1
        type(self)._inited = True

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x


# another option is to use decorator
# the problem is that C is no longer a class, it's a function
def singleton(cls):
    inst = cls()

    def get_instance():
        return inst

    return get_instance


@singleton
class C:
    def __init__(self) -> None:
        self.x = 1


# another option is to use metaclass
# not thread-safe
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.x = 1

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x


# thread-safe
class SingletonMetaThreadSafe(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonThreadSafe(metaclass=SingletonMetaThreadSafe):
    def __init__(self, value: int) -> None:
        self.value = value

    def increment_thing(self) -> None:
        self.value += 1

    def get_thing(self) -> int:
        return self.value


def test_singleton(value: int) -> None:
    singleton = SingletonThreadSafe(value)
    print(singleton.value)


def main() -> None:
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    process1 = Thread(target=test_singleton, args=(1,))
    process2 = Thread(target=test_singleton, args=(2,))
    process1.start()
    process2.start()


if __name__ == "__main__":
    main()

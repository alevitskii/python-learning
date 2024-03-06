import collections
from typing import NamedTuple

# User = collections.namedtuple("User", ("name", "age", "location"))


# In order to attach methods you need to inherit like this
class User(collections.namedtuple("User", ("name", "age", "location"))):
    __slots__ = ()

    def print_me(self):
        print(f"{self.name} is {self.age} years old and from {self.location}")


# Newer (preferable) way to create named tuples
class User2(NamedTuple):
    name: str
    age: int
    location: str = "unknown"

    def print_me(self):
        print(f"{self.name} is {self.age} years old and from {self.location}")


def get_users():
    return [
        User("Anothony", 29, "CA"),
        User("Jeff", 29, "NY"),
        User("Jason", 29, "GB"),
        User2("Anothony", 29, "CA"),
        User2("Jeff", 29, "NY"),
        User2("Carmen San Diego", 32),
    ]


# this functions is to build something like property
# @property
# def {name}(self):
#     return self[idx]
def _make_named_attr_getter(idx: int, name: str):
    def getter(self):
        return self[idx]

    getter.__name__ = name
    return property(getter)


def _namedtuple_rerp(self) -> str:
    fields_s = ", ".join(f"{name}={getattr(self, name)!r}" for name in self._fields)
    return f"{type(self).__name__}({fields_s})"


# Our own implementation of the old named tuple
def make_namedtuple(clsname, fields):
    attrs = {"_fields": fields, "__repr__": _namedtuple_rerp}

    # make the initialization
    new_method_s = f"""
def __new__(cls, {', '.join(fields)}):
    return tuple.__new__(cls, ({", ".join(fields)}))
"""
    # exec is unsafe so before executing this lots of validations
    # need to be performed
    exec(new_method_s, attrs)

    for idx, name in enumerate(fields):
        attrs[name] = _make_named_attr_getter(idx, name)

    return type(clsname, (tuple,), attrs)


class User3(make_namedtuple("User", ("name", "age", "location"))):
    __slots__ = ()

    def print_me(self):
        print(f"{self.name} is {self.age} years old and from {self.location}")


# this is what the class would look like if we had written it manually without generation
class User4(tuple):
    _fields = ("name", "age", "location")

    def __new__(cls, name, age, location):
        return tuple.__new__(cls, (name, age, location))

    @property
    def name(self):
        return self[0]

    @property
    def age(self):
        return self[1]

    @property
    def location(self):
        return self[2]

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, age={self.age}, location={self.location})"

    def print_me(self):
        print(f"{self.name} is {self.age} years old and from {self.location}")


def get_users2():
    return [
        User3("Anothony", 29, "CA"),
        User3("Jeff", 29, "NY"),
        User3("Jason", 29, "GB"),
        # User3("Carmen San Diego", 32),
    ]


def main() -> None:
    # for name, age, location in get_users():
    #     print(f"{name} is {age} years old and from {location}")
    # for user in get_users():
    #     print(f"{user.name} is {user.age} years old and from {user.location}")
    # for user in get_users():
    #     user.print_me()
    #     # named tuples are immutable
    #     # user.name = "qq"
    #     # although the method starts with _, it's not treated as private
    #     # it's just the way named tuple defines its method names
    #     print(user._asdict())

    for user in get_users2():
        user.print_me()
        print(repr(user))


if __name__ == "__main__":
    main()

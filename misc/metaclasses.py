class Meta(type):
    # overriding the new method of the metaclass
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        # defining that each class with this metaclass
        # should have a variable, x with a default value
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass


def main() -> None:
    # printing the variables in our newly defined class
    print(Foo.attr)


if __name__ == "__main__":
    main()

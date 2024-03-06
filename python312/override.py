from typing import override


class C:
    def new_frob(self):
        print("default")

    def do_work(self):
        self.new_frob()


class D(C):
    # override explicitly saying that this method is supposed to be the base class
    # @override
    def frob(self):
        print("something else")


def main() -> None:
    pass


if __name__ == "__main__":
    main()

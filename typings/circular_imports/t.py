from a import A
from b import B


def main() -> None:
    a_inst = A()
    b_inst = B()
    a_inst.foo(b_inst)


if __name__ == "__main__":
    main()

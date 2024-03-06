import dis


def f():
    x = [i * 2 for i in range(5)]
    return x


def main() -> None:
    # before 3.12 compehension were technically separate functions "attached"
    # to the main function, and they were called
    # now it's inlined, and faster, the whole thing is happening between
    # LOAD_FAST_AND_CLEAR i and STORE_FAST i
    dis.dis(f)


if __name__ == "__main__":
    main()

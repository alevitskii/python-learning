import itertools


def main() -> None:
    it = range(1, 10)
    for a, b, c in itertools.batched(it, 3):
        print(a, b, c)

    # will throw an error in the end
    it = range(1, 10)
    for a, b in itertools.batched(it, 2):
        print(a, b)


if __name__ == "__main__":
    main()

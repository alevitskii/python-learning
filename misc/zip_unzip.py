import itertools


def main() -> None:
    ranks = list(range(1, 6))
    colors = ["orange", "yellow", "blue", "green", "red", "purple"]
    for idx, color in zip(ranks, colors):
        print(f"{idx=} {color=}")

    # will throw an error
    # for idx, color in zip(ranks, colors, strict=True):
    #     print(f"{idx=} {color=}")

    for idx, color in itertools.zip_longest(ranks, colors, fillvalue=-1):
        print(f"{idx=} {color=}")

    lst = list(zip(ranks, colors))
    # COOL!
    print(list(zip(*lst)))


if __name__ == "__main__":
    main()

def main() -> None:
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3, 4, 5]
    for x, y in zip(lst1, lst2, strict=True):
        print(f"{x=}, {y=}")


if __name__ == "__main__":
    main()

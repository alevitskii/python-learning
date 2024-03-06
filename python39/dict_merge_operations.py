def main() -> None:
    d1 = {1: 2, 3: 4}
    d2 = {5: 6, 7: 8}
    d3 = {1: 999, 999: 1}
    print(d1 | d2)
    print(d1 | d3)
    d3 |= d1
    print(d3)


if __name__ == "__main__":
    main()

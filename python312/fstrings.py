def main() -> None:
    hi = 3
    print(f'hi{f'{hi}'}')
    print(f'hi{
        3  # hi
    }')


if __name__ == "__main__":
    main()

from collections.abc import Generator


def generate_numbers_2_yields() -> Generator[int, int, None]:
    i = 0
    while True:
        i += 1
        yield i
        k = yield  # type: ignore
        print(f"Received in generator function: {k}")


def generate_numbers_combined() -> Generator[int, int, None]:
    i = 0
    while True:
        i += 1
        k = yield i
        print(f"Received in generator function: {k}")


def main() -> None:
    # 1st example
    generator = generate_numbers_2_yields()

    # The first iteration happens outside the loop
    item = next(generator)
    print(f"[outside] Received in main function: {item}")

    for i in range(0, 5):
        # The noop operation required to move the generator from the first yield to the second yield statement
        next(generator)
        # send will both pass in the value to the generator function and also yield the next value from the generator
        item = generator.send(i + 50)
        print(f"[{i}] Received in main function: {item}")

    # 2nd example
    generator = generate_numbers_combined()

    # item = generator.send(None)
    item = next(generator)
    print(f"[outside] Received in main function: {item}")

    for i in range(0, 5):
        item = generator.send(55 + i)
        print(f"[{i}] Received in main function: {item}")


if __name__ == "__main__":
    main()

from collections.abc import Generator


# Anytime you return from a generator function, it'll be equivalent of raising the StopIteration exception
def function() -> Generator[str, None, str]:
    yield "Test1"
    return "Test2"


def get_item() -> Generator[int]:
    try:
        yield 5
    except GeneratorExit:
        print("GeneratorExit exception raised")


def main() -> None:
    # 1st example
    gen = function()
    print(next(gen))
    try:
        next(gen)
    except StopIteration as e:
        print(f"Got from exception {e.value}")  # returned value saved in e.value

    # 2nd example
    gen2 = get_item()
    print(next(gen2))
    # gen2.close()  # will show "GeneratorExit exception raised" here because invoke manually
    print("Main exiting")
    # will show "GeneratorExit exception raised" after "Main exiting"
    # because garbage collector will invoke close() on the generator


if __name__ == "__main__":
    main()

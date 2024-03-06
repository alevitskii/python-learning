import functools


@functools.lru_cache(maxsize=3)
def square(x: float) -> float:
    print(f"running: {x}")
    return x * x


# this acts like a function returning singleton
@functools.lru_cache(maxsize=1)
def get_thing() -> int:
    # pretend this is expensive
    print("expensive")
    return 42

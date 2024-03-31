# the reason you shouldn't decorate compute with lru_cache is
# it'll keep a reference to self and won't let it be garbage collected
# you can make a cache per instance, not per class but in this case
# you'll have to recompute even if you create instances with the same arguments
# solution to this might be creating a pool of objects
# another solution is to make `compute` a function, not a method and
# don't pass an instance to it
import functools
import time


class C:
    def __init__(self, y: int) -> None:
        self.y = y
        self.compute = functools.lru_cache(maxsize=None)(self._compute_uncached)

    def _compute_uncached(self, x: int) -> int:
        print("computing ...")
        time.sleep(0.5)
        return self.y * x * x

    def __del__(self) -> None:
        print(f"deleting {self}...")


def main() -> None:
    c = C(10)
    print(c.compute(4))
    print(c.compute(4))

    print(C(20).compute(4))
    print(C(20).compute(4))


if __name__ == "__main__":
    main()

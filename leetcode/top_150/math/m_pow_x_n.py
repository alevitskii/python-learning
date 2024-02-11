from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        return self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, n % 2)


def main() -> None:
    inputs = [
        (2.00000, 10),
        (2.10000, 3),
        (2.00000, -2),
    ]
    s = Solution()
    for x, n in inputs:
        print(s.myPow(x, n))


if __name__ == "__main__":
    main()

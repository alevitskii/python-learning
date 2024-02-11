import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes, power_of_five = 0, 5
        while n // power_of_five:
            zeroes += n // power_of_five
            power_of_five *= 5
        return zeroes


def main() -> None:
    inputs = [
        # 3,
        # 5,
        # 0,
        17,
        125,
    ]
    s = Solution()
    for n in inputs:
        print(s.trailingZeroes(n))


if __name__ == "__main__":
    main()

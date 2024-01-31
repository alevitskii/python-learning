import math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes, power_of_five = 0, 5
        while n // power_of_five:
            zeroes += n // power_of_five
            power_of_five *= 5
        return zeroes


if __name__ == "__main__":
    inputs = [
        # 3,
        # 5,
        # 0,
        17
    ]
    s = Solution()
    for n in inputs:
        print(s.trailingZeroes(n))

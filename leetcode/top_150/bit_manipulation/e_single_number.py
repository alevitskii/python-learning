from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor


def main() -> None:
    inputs = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]
    s = Solution()
    for n in inputs:
        print(s.singleNumber(n))


if __name__ == "__main__":
    main()

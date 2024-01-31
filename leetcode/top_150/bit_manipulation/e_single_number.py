from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor


if __name__ == "__main__":
    inputs = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]
    s = Solution()
    for n in inputs:
        print(s.singleNumber(n))

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return d[target - n], i
            d[n] = i


if __name__ == "__main__":
    inputs = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    s = Solution()
    for nums, target in inputs:
        print(s.twoSum(nums, target))

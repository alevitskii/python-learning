from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(idx, total):
            if idx == len(nums):
                return total == target
            if (idx, total) in dp:
                return dp[(idx, total)]
            dp[(idx, total)] = backtrack(idx + 1, total + nums[idx]) + backtrack(idx + 1, total - nums[idx])
            return dp[(idx, total)]

        dp = {}
        return backtrack(0, 0)


if __name__ == "__main__":
    inputs = [
        ([1, 1, 1, 1, 1], 3),
        ([1], 1),
    ]
    s = Solution()
    for nums, target in inputs:
        print(s.findTargetSumWays(nums, target))

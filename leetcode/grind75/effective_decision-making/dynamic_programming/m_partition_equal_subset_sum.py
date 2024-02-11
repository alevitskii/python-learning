from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def recursive(sum1, sum2, index):
            if sum1 > subset_sum or sum2 > subset_sum:
                return False
            if index == len(nums):
                return sum1 == sum2
            return recursive(sum1 + nums[index], sum2, index + 1) or recursive(sum1, sum2 + nums[index], index + 1)

        total = sum(nums)
        if total % 2:
            return False
        subset_sum = total // 2
        return recursive(0, 0, 0)


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def recursive(subset_sum, index):
            if index >= len(nums):
                return False
            if subset_sum == target:
                return True
            return recursive(subset_sum + nums[index], index + 1) or recursive(subset_sum, index + 1)

        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        return recursive(0, 0)


class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        array_sum = sum(nums)
        if array_sum % 2 != 0:
            return False
        subset_sum = array_sum // 2
        dp = [[False for i in range(len(nums) + 1)] for j in range(subset_sum + 1)]
        for idx in range(0, len(nums) + 1):
            dp[0][idx] = True
        for target in range(1, subset_sum + 1):
            for idx in range(1, len(nums) + 1):
                if nums[idx - 1] > target:
                    dp[target][idx] = dp[target][idx - 1]
                else:
                    dp[target][idx] = dp[target - nums[idx - 1]][idx - 1] or dp[target][idx - 1]
        return dp[subset_sum][len(nums)]


class Solution4:
    def canPartition(self, nums: List[int]) -> bool:
        array_sum = sum(nums)
        if array_sum % 2 != 0:
            return False
        subset_sum = array_sum // 2
        dp = [[False] * (subset_sum + 1) for _ in range(len(nums))]
        for i in range(0, len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for idx in range(1, len(nums)):
            for target in range(1, subset_sum + 1):
                not_take = dp[idx - 1][target]
                take = False
                if nums[idx] <= target:
                    take = dp[idx - 1][target - nums[idx]]
                dp[idx][target] = take or not_take
        return dp[len(nums) - 1][subset_sum]


def main() -> None:
    inputs = [
        # [1, 5, 11, 5],
        # [1, 2, 3, 5],
        [1, 3, 7, 3],
    ]
    s = Solution3()
    for string in inputs:
        print(s.canPartition(string))


if __name__ == "__main__":
    main()

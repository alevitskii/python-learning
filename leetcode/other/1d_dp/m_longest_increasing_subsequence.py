from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left

        result = [nums[0]]
        for n in nums:
            if n <= result[-1]:
                i = bisect_left(result, n)
                result[i] = n
            else:
                result.append(n)
        return len(result)


def main() -> None:
    inputs = [
        [10, 9, 2, 5, 1, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 0, 1, 0, 2],
        [7, 7, 7, 7, 7, 7, 7],
        [1, 2, 3, 0, 2],
    ]
    s = Solution2()
    for nums in inputs:
        print(s.lengthOfLIS(nums))


if __name__ == "__main__":
    main()

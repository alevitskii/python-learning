from typing import List


# Kadane's algorithm
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_prev, maxs = 0, nums[0]
        min_prev, mins = 0, nums[0]
        for i in nums:
            max_prev = max(i + max_prev, i)
            min_prev = min(i + min_prev, i)
            maxs = max(maxs, max_prev)
            mins = min(mins, min_prev)
            total += i
        return max(maxs, total - mins) if maxs > 0 else maxs


def main() -> None:
    inputs = [
        [1, -2, 3, -2],
        [5, -3, 5],
        [-3, -2, -3],
    ]
    s = Solution()
    for nums in inputs:
        print(s.maxSubarraySumCircular(nums))


if __name__ == "__main__":
    main()

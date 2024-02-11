from math import inf
from typing import List


# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev, maxs = nums[0], nums[0]
        for i in nums[1:]:
            prev = max(i + prev, i)
            maxs = max(maxs, prev)
        return maxs


# Divide & Conquer
class Solution2:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R:
                return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid - 1, L - 1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid + 1, R + 1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid - 1), maxSubArray(A, mid + 1, R), left_sum + A[mid] + right_sum)

        return maxSubArray(nums, 0, len(nums) - 1)


# D&C optimized
class Solution3:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L == R:
                return A[L]
            mid = (L + R) // 2
            return max(maxSubArray(A, L, mid), maxSubArray(A, mid + 1, R), pre[mid] + suf[mid + 1])

        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):
            pre[i] += max(0, pre[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            suf[i] += max(0, suf[i + 1])
        return maxSubArray(nums, 0, len(nums) - 1)


def main() -> None:
    inputs = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
    ]
    s = Solution2()
    for nums in inputs:
        print(s.maxSubArray(nums))


if __name__ == "__main__":
    main()

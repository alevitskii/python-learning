from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        max_sum = nums[0]
        current_sum = 0
        while left < len(nums):
            while right < len(nums) and nums[right] + current_sum > 0:
                current_sum += nums[right]
                max_sum = max(max_sum, current_sum)
                right += 1
            max_sum = max(max_sum, nums[left])
            left = right + 1
            right = left
            current_sum = 0
        return max_sum


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        prev, max_ = nums[0], nums[0]

        for i in nums[1:]:
            prev = max(i + prev, i)
            max_ = max(max_, prev)

        return max_


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArray(A, L, R):
            if L > R:
                return -(10**5)
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid - 1, L - 1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid + 1, R + 1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid - 1), maxSubArray(A, mid + 1, R), left_sum + A[mid] + right_sum)

        return maxSubArray(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    inputs = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        # [1],
        # [5, 4, -1, 7, 8],
        # [-2, -1]
    ]
    s = Solution()
    s1 = Solution1()
    s2 = Solution2()
    for nums in inputs:
        print(s.maxSubArray(nums))
        print(s1.maxSubArray(nums))
        print(s2.maxSubArray(nums))

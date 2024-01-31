from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def construct_range(left, right):
            return f"{left}->{right}" if left < right else str(left)

        if not nums:
            return nums

        left, right = nums[0], nums[0]
        result = []
        for i in range(1, len(nums)):
            if nums[i] - right > 1:
                result.append(construct_range(left, right))
                left = nums[i]
            right = nums[i]
        return result + [construct_range(left, right)]


if __name__ == "__main__":
    inputs = [
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9, 10],
        [0, 1],
        [],
    ]
    s = Solution()
    for nums in inputs:
        print(s.summaryRanges(nums))

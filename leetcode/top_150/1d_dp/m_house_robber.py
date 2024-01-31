from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # nums[1] = max(nums[0], nums[1] + 0)
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        return nums[-1] if len(nums) > 2 else max(nums)


if __name__ == "__main__":
    inputs = [
        # [1, 2, 3, 1],
        # [2, 7, 9, 3, 1],
        [1],
        # [1, 2, 3, 4],
        [2, 1],
        [2, 1, 1, 2],
    ]
    s = Solution()
    for nums in inputs:
        print(s.rob(nums))

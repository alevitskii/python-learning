from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2


if __name__ == "__main__":
    inputs = [[1, 2, 3, 1], [2, 7, 9, 3, 1], [2], [1, 2], [2, 1, 1, 2]]
    s = Solution2()
    for nums in inputs:
        print(s.rob(nums))

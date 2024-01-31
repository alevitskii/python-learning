from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i != nums[i] and nums[i] < len(nums):
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


if __name__ == "__main__":
    inputs = [
        # [0, 1, 2, 4],
        [3, 0, 1, 4],
        [1, 0, 2, 3, 4, 5, 6, 8, 9, 7, 11],
    ]
    s = Solution()
    for nums in inputs:
        print(s.missingNumber(nums))

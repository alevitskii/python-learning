from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx] or nums[i] != nums[idx - 1]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1 if idx != 0 and len(nums) > 2 else 2


class Solution2:
    def removeDuplicates(self, nums):
        idx = 0
        for n in nums:
            if idx < 2 or n != nums[idx - 2]:
                nums[idx] = n
                idx += 1
        return idx


if __name__ == "__main__":
    inputs = [
        [1, 1, 1, 2, 2, 3],  # [1, 1, 2, 2, 3, _], 5
        [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3],  # [0, 0, 1, 1, 2, 3, 3, _, _], 7
        [0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4],
        [0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3],
        [1, 1],
        [1],
    ]
    s = Solution2()
    for nums in inputs:
        print(s.removeDuplicates(nums))
        print(nums)

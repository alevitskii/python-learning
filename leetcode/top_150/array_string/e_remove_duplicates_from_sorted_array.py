from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1
        return idx


if __name__ == "__main__":
    inputs = [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [1, 1, 2]]  # [0, 1, 2, 3, 4, _, _, _, _, _], 5
    s = Solution()
    s2 = Solution2()
    for nums in inputs:
        print(s2.removeDuplicates(nums))
        print(nums)

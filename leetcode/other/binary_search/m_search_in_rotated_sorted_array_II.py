from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                if len(set(nums[left : mid + 1])) == 1:
                    left = mid + 1
                    continue
            elif nums[right] == nums[mid]:
                if len(set(nums[mid : right + 1])) == 1:
                    right = mid - 1
                    continue
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True
            if left < len(nums) - 1 and nums[left] == nums[right]:
                left += 1
                continue
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == "__main__":
    inputs = [([2, 5, 6, 0, 0, 1, 2], 0), ([2, 5, 6, 0, 0, 1, 2], 3), ([1, 0, 1, 1, 1], 0), ([3, 1], 1)]
    s = Solution2()
    for nums, target in inputs:
        print(s.search(nums, target))

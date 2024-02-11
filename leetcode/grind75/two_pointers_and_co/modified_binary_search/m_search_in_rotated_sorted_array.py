from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
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
        return -1


class Solution2:
    def binary_search(self, nums, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                return self.binary_search(nums, low, mid - 1, target)
            return self.binary_search(nums, mid + 1, high, target)
        else:
            if nums[mid] < target and target <= nums[high]:
                return self.binary_search(nums, mid + 1, high, target)
            return self.binary_search(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)


def main() -> None:
    inputs = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
    ]

    s = Solution2()
    for nums, target in inputs:
        print(s.search(nums, target))


if __name__ == "__main__":
    main()

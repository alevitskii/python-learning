from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        left, right = 1, len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


def main() -> None:
    inputs = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1, 2, 3],
    ]
    s = Solution()
    for nums in inputs:
        print(s.findPeakElement(nums))


if __name__ == "__main__":
    main()

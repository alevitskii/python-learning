from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    return nums[left]
            else:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    return nums[right]
        return nums[left]


def main() -> None:
    inputs = [[3, 4, 5, 1, 2], [4, 5, 6, 7, 0, 1, 2], [7, 8, 9, 0, 1, 2, 3, 4], [11, 13, 15, 17], [5, 1, 2, 3, 4]]
    s = Solution()
    for nums in inputs:
        print(s.findMin(nums))


if __name__ == "__main__":
    main()

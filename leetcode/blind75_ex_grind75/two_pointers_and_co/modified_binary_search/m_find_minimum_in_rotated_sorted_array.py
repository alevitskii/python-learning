from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while True:
            mid = (left + right) >> 1
            left_el, mid_el, right_el = nums[left], nums[mid], nums[right]
            if left_el <= mid_el:
                if mid_el <= right_el:
                    return left_el
                left = mid + 1
            else:
                right = mid


class Solution2:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == "__main__":
    inputs = [[3, 4, 5, 1, 2], [4, 5, 6, 7, 0, 1, 2], [7, 8, 9, 0, 1, 2, 3, 4], [11, 13, 15, 17], [5, 1, 2, 3, 4]]
    s = Solution()
    for nums in inputs:
        print(s.findMin(nums))

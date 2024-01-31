class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) >> 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    inputs = [
        ([-1, 0, 3, 5, 9, 12], 9),
        ([-1, 0, 3, 5, 9, 12], 2),
    ]
    s = Solution()
    for nums, target in inputs:
        print(s.search(nums, target))

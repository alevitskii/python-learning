from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                result = [None, None]
                sub_left, sub_right = left, mid
                while sub_left <= sub_right:
                    sub_mid = (sub_right + sub_left) // 2
                    if nums[sub_mid] != target:
                        sub_left = sub_mid + 1
                    else:
                        sub_right = sub_mid - 1
                result[0] = sub_left

                sub_left, sub_right = mid, right
                while sub_left <= sub_right:
                    sub_mid = (sub_right + sub_left) // 2
                    if nums[sub_mid] != target:
                        sub_right = sub_mid - 1
                    else:
                        sub_left = sub_mid + 1
                result[1] = sub_right

                return result
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]


def main() -> None:
    inputs = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 3),
        ([], 0),
    ]
    s = Solution()
    for nums, target in inputs:
        print(s.searchRange(nums, target))


if __name__ == "__main__":
    main()

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        stored_water = 0
        left_max, right_max = 0, 0
        while left <= right:
            if left_max > right_max:
                stored_water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
            else:
                stored_water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
        return stored_water


if __name__ == "__main__":
    inputs = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
    ]

    s = Solution()
    for height in inputs:
        print(s.trap(height))

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                right_boundary = i
                left_boundary = stack[-1]
                current_width = right_boundary - left_boundary - 1
                current_area = current_height * current_width
                max_area = max(max_area, current_area)
            stack.append(i)
        n = len(heights)
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            left_boundary = stack[-1]
            current_width = n - stack[-1] - 1
            current_area = current_height * current_width
            max_area = max(max_area, current_area)
        return max_area


if __name__ == "__main__":
    inputs = [
        [2, 4, 5, 7, 3, 9],
        # [2, 1, 5, 6, 2, 3],
        [2, 4],
    ]
    s = Solution()
    for heights in inputs:
        print(s.largestRectangleArea(heights))

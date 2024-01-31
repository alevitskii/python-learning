from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False
        left, right = 0, len(matrix[0]) - 1
        row = mid
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == "__main__":
    inputs = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        ([[1]], 2),
    ]
    s = Solution()
    for matrix, target in inputs:
        print(s.searchMatrix(matrix, target))

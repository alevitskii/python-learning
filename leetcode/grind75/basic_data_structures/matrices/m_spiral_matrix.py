from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, -1
        direction = 1
        result = []
        while rows > 0 and cols > 0:
            for _ in range(cols):
                col += direction
                result.append(matrix[row][col])
            rows -= 1
            for _ in range(rows):
                row += direction
                result.append(matrix[row][col])
            cols -= 1
            direction *= -1
        return result


def main() -> None:
    inputs = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    s = Solution()
    for matrix in inputs:
        print(s.spiralOrder(matrix))


if __name__ == "__main__":
    main()

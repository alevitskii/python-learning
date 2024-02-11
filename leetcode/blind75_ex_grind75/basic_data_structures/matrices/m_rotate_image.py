class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


class Solution2:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # Traverse the matrix
        for row in range(n // 2):
            for col in range(row, n - row - 1):
                # Swap the top-left and top-right cells in the current group
                matrix[row][col], matrix[col][n - 1 - row] = matrix[col][n - 1 - row], matrix[row][col]
                # Swap the top-left and bottom-right cells in the current group
                matrix[row][col], matrix[n - 1 - row][n - 1 - col] = matrix[n - 1 - row][n - 1 - col], matrix[row][col]
                # Swap the top-left and bottom-left cells in the current group
                matrix[row][col], matrix[n - 1 - col][row] = matrix[n - 1 - col][row], matrix[row][col]


def main() -> None:
    inputs = [
        # [[1, 2, 3],
        #  [4, 5, 6],
        #  [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ]
    s = Solution2()
    for matrix in inputs:
        s.rotate(matrix)
        print(matrix)


if __name__ == "__main__":
    main()

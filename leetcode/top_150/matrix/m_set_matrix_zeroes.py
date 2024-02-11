from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for ii in range(m):
                        if matrix[ii][j] != 0:
                            matrix[ii][j] = None
                    for jj in range(n):
                        if matrix[i][jj] != 0:
                            matrix[i][jj] = None
                    matrix[i][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        fcol, frow = False, False
        for i in range(rows):
            if matrix[i][0] == 0:
                fcol = True
        for i in range(cols):
            if matrix[0][i] == 0:
                frow = True
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        if fcol:
            for i in range(rows):
                matrix[i][0] = 0
        if frow:
            for j in range(cols):
                matrix[0][j] = 0
        return matrix


def main() -> None:
    inputs = [
        # [[1, 1, 1],
        #  [1, 0, 1],
        #  [1, 1, 1]],
        # [[0, 1, 2, 0],
        #  [3, 4, 5, 2],
        #  [1, 3, 1, 5]],
        [[3, 5, 2, 0], [1, 0, 4, 0], [7, 3, 2, 4]],
    ]
    s = Solution2()
    for matrix in inputs:
        print(s.setZeroes(matrix))
        print(matrix)


if __name__ == "__main__":
    main()

from collections import deque
from typing import List


class SolutionDFS:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[10**5] * len(mat[0]) for _ in mat]

        def dfs(mat, i, j, d, res):
            if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
                return
            if d < res[i][j]:
                res[i][j] = d
                dfs(mat, i - 1, j, d + 1, res)
                dfs(mat, i, j - 1, d + 1, res)
                dfs(mat, i + 1, j, d + 1, res)
                dfs(mat, i, j + 1, d + 1, res)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dfs(mat, i, j, 0, res)
        return res


class SolutionBFS:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX_VALUE = m * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat


class SolutionDP:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col] > 0:
                    above = mat[row - 1][col] if row > 0 else float("inf")
                    left = mat[row][col - 1] if col > 0 else float("inf")
                    mat[row][col] = min(above, left) + 1
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if mat[row][col] > 0:
                    below = mat[row + 1][col] if row < m - 1 else float("inf")
                    right = mat[row][col + 1] if col < n - 1 else float("inf")
                    mat[row][col] = min(mat[row][col], below + 1, right + 1)
        return mat


if __name__ == "__main__":
    inputs = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
    ]
    s = SolutionDP()
    for mat in inputs:
        print(s.updateMatrix(mat))

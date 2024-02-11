from functools import cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(r, c):
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]
            if r < len(grid) and c < len(grid[0]):
                return grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return 1000

        return dfs(0, 0)


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[1000] * (len(grid[0]) + 1) for _ in range(len(grid) + 1)]
        dp[len(grid) - 1][len(grid[0])] = 0
        dp[len(grid)][len(grid[0]) - 1] = 0
        for r in range(len(grid) - 1, -1, -1):
            for c in range(len(grid[0]) - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]


def main() -> None:
    inputs = [
        [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        [[1, 2, 3], [4, 5, 6]],
    ]
    s = Solution2()
    for grid in inputs:
        print(s.minPathSum(grid))


if __name__ == "__main__":
    main()

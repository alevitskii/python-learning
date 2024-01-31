from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def within_bound(r, c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

        def dfs(r, c, prev_val):
            if not within_bound(r, c) or matrix[r][c] <= prev_val:
                return 0
            if (r, c) in dp:
                return dp[((r, c))]
            res = 1
            for rs, cs in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res = max(res, dfs(r + rs, c + cs, matrix[r][c]) + 1)
            dp[(r, c)] = res
            return res

        dp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)
        return max(dp.values())


if __name__ == "__main__":
    inputs = [[[9, 9, 4], [6, 6, 8], [2, 1, 1]], [[3, 4, 5], [3, 2, 6], [2, 2, 1]], [[1]]]
    s = Solution()
    for matrix in inputs:
        print(s.longestIncreasingPath(matrix))

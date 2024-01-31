from functools import cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def descend(triangle, ilevel, ipath, dp, pathl):
            if ilevel >= len(triangle) or ipath < 0 or ipath >= len(triangle[ilevel]):
                return
            path = triangle[ilevel][ipath]
            if ipath not in dp[ilevel] or dp[ilevel][ipath] > pathl + path:
                dp[ilevel][ipath] = pathl + path
                descend(triangle, ilevel + 1, ipath, dp, dp[ilevel][ipath])
                descend(triangle, ilevel + 1, ipath + 1, dp, dp[ilevel][ipath])

        dp = [{} for _ in range(len(triangle))]
        descend(triangle, 0, 0, dp, 0)
        return min(dp[-1].values())


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        levels = len(triangle)
        dp = [[0] * (levels + 1) for _ in range(levels + 1)]
        for level in range(levels - 1, -1, -1):
            for i in range(level + 1):
                dp[level][i] = triangle[level][i] + min(dp[level + 1][i], dp[level + 1][i + 1])
        return dp[0][0]


class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(level, i):
            return 0 if level >= len(triangle) else triangle[level][i] + min(dfs(level + 1, i), dfs(level + 1, i + 1))

        return dfs(0, 0)


if __name__ == "__main__":
    inputs = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-10]],
    ]
    s = Solution3()
    for triangle in inputs:
        print(s.minimumTotal(triangle))

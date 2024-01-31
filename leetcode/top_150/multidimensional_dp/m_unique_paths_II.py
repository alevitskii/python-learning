from functools import cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        previous = [0] * len(obstacleGrid[0])
        previous[0] = 1
        for r, current in enumerate(obstacleGrid):
            current[0] = previous[0] if obstacleGrid[r][0] != 1 else 0
            for i in range(1, len(current)):
                current[i] = current[i - 1] + previous[i] if current[i] != 1 else 0
            previous = current
        return current[-1]


if __name__ == "__main__":
    inputs = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 1], [0, 0]], [[0, 0], [0, 1]], [[0, 1], [1, 0]]]
    s = Solution()
    for obstacleGrid in inputs:
        print(s.uniquePathsWithObstacles(obstacleGrid))

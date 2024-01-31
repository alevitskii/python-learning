from collections import deque
from typing import List

from m_number_of_islands_helper import UnionFind


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            nonlocal grid
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)

        answer = 0
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        dfs(i, j)
                        answer += 1
            else:
                break
        return answer


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        def within_bound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left
        count = 0
        queue = deque()
        for ri in range(len(grid)):
            for ci in range(len(grid[0])):
                if grid[ri][ci] == "1":
                    grid[ri][ci] = "0"
                    count += 1
                    queue.append([ri, ci])
                    while queue:
                        r, c = queue.popleft()
                        for rd, cd in DIRECTIONS:
                            nr, nc = r + rd, c + cd
                            if within_bound(nr, nc) and grid[nr][nc] == "1":
                                queue.append([nr, nc])
                                grid[nr][nc] = "0"
        return count


class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        cols = len(grid[0])
        rows = len(grid)
        union_find = UnionFind(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"

                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        union_find.union(r * cols + c, (r - 1) * cols + c)
                    if r + 1 < rows and grid[r + 1][c] == "1":
                        union_find.union(r * cols + c, (r + 1) * cols + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        union_find.union(r * cols + c, r * cols + c - 1)
                    if c + 1 < cols and grid[r][c + 1] == "1":
                        union_find.union(r * cols + c, r * cols + c + 1)

        count = union_find.get_count()
        return count


if __name__ == "__main__":
    inputs = [
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
    ]
    s = Solution3()
    for grid in inputs:
        print(s.numIslands(grid))

from collections import deque
from typing import List


class Solution:
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


if __name__ == "__main__":
    inputs = [
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
    ]
    s = Solution()
    for grid in inputs:
        print(s.numIslands(grid))

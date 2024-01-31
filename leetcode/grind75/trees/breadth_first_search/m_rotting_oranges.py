from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left
        fresh = 0
        rotten = []
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == 1:
                    fresh += 1
                elif grid[row_idx][col_idx] == 2:
                    rotten.append([row_idx, col_idx])
        current_queue_size = len(rotten)
        minutes = 0
        while len(rotten) > 0:
            if current_queue_size == 0:
                minutes += 1
                current_queue_size = len(rotten)
            row, col = rotten.pop(0)
            current_queue_size -= 1
            for row_shift, col_shift in DIRECTIONS:
                new_row, new_col = row + row_shift, col + col_shift
                if (
                    new_row < 0
                    or new_row >= len(grid)
                    or new_col < 0
                    or new_col >= len(grid[0])
                    or grid[new_row][new_col] in {0, 2}
                ):
                    continue
                grid[new_row][new_col] = 2
                fresh -= 1
                rotten.append([new_row, new_col])
        return -1 if fresh > 0 else minutes


if __name__ == "__main__":
    inputs = [
        [[2, 1, 1], [1, 1, 0], [0, 1, 1]],
        [[2, 1, 1], [0, 1, 1], [1, 0, 1]],
        [[0, 2]],
    ]
    s = Solution()
    for grid in inputs:
        print(s.orangesRotting(grid))

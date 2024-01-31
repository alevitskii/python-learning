from collections import deque
from typing import List


class Solution:
    def get_coordinates(self, pos, n):
        row = n - pos // n - (1 if pos % n else 0)
        direction = -1 if (n - row - 1) % 2 else 1
        col = direction * (pos % n) - (0 if direction == -1 else 1)
        return row, col

    def determine_steps(self, steps_range, board):
        steps = set()
        max_simple = None
        for pos in range(steps_range[1], steps_range[0] - 1, -1):
            r, c = self.get_coordinates(pos, len(board))
            if board[r][c] != -1:
                nr, nc = self.get_coordinates(board[r][c], len(board))
                steps.add((nr, nc, board[r][c]))
            elif not max_simple:
                max_simple = (r, c, pos)
        if max_simple:
            steps.add(max_simple)
        return list(steps)

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue, seen = deque(), set()
        queue.extend(self.determine_steps([2, min(7, n**2)], board))
        round_number = 1
        while queue:
            count, length = 0, len(queue)
            while count < length:
                count += 1
                _, __, pos = queue.popleft()
                if pos in seen:
                    continue
                seen.add(pos)
                if pos == n**2:
                    return round_number
                queue.extend(self.determine_steps([pos + 1, min(pos + 6, n**2)], board))
            round_number += 1
        return -1


class Solution2:
    def get_coordinates(self, pos, n):
        row = n - pos // n - (1 if pos % n else 0)
        direction = -1 if (n - row - 1) % 2 else 1
        col = direction * (pos % n) - (0 if direction == -1 else 1)
        return row, col

    def determine_steps(self, steps_range, board):
        steps = set()
        max_simple = None
        for pos in range(steps_range[1], steps_range[0] - 1, -1):
            r, c = self.get_coordinates(pos, len(board))
            if board[r][c] != -1:
                steps.add(board[r][c])
            elif not max_simple:
                max_simple = pos
        if max_simple:
            steps.add(max_simple)
        return list(steps)

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue, seen = deque(), set()
        queue.extend(self.determine_steps([2, min(7, n**2)], board))
        round_number = 1
        while queue:
            count, length = 0, len(queue)
            while count < length:
                count += 1
                pos = queue.popleft()
                if pos in seen:
                    continue
                seen.add(pos)
                if pos == n**2:
                    return round_number
                queue.extend(self.determine_steps([pos + 1, min(pos + 6, n**2)], board))
            round_number += 1
        return -1


if __name__ == "__main__":
    inputs = [
        [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ],
        [[-1, -1], [-1, 3]],
        [[-1, 4, -1], [6, 2, 6], [-1, 3, -1]],
        [[1, 1, -1], [1, 1, 1], [-1, 1, 1]],
    ]
    s = Solution2()
    for board in inputs:
        print(s.snakesAndLadders(board))

from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def within_bound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def on_border(r, c):
            return r in (0, len(board) - 1) or c in (0, len(board[0]) - 1)

        DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left
        queue = deque()
        seen = set()
        for ri in range(len(board)):
            for ci in range(len(board[0])):
                if board[ri][ci] == "O" and (ri, ci) not in seen:
                    queue.append([ri, ci])
                    flip_cadidates = {(ri, ci)}
                    dont_flip = False
                    while queue:
                        r, c = queue.popleft()
                        dont_flip = dont_flip or on_border(r, c)
                        for rd, cd in DIRECTIONS:
                            nr, nc = r + rd, c + cd
                            if within_bound(nr, nc) and board[nr][nc] == "O" and (nr, nc) not in flip_cadidates:
                                dont_flip = dont_flip or on_border(nr, nc)
                                flip_cadidates.add((nr, nc))
                                queue.append([nr, nc])
                    if dont_flip:
                        seen |= flip_cadidates
                    else:
                        for fr, fc in flip_cadidates:
                            board[fr][fc] = "X"


if __name__ == "__main__":
    inputs = [
        [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
        [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]],
        [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]],
        [["X"]],
    ]
    s = Solution()
    for board in inputs:
        s.solve(board)
        print(board)

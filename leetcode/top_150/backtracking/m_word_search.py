from collections import defaultdict
from typing import List

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


class Solution:
    def withing_board(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n

    def exist(self, board: List[List[str]], word: str) -> bool:
        def recursion(board, row, col, word, seen):
            if len(word) == 0:
                return True
            char = word[0]
            for r, c in DIRECTIONS:
                nr, nc = row + r, col + c
                if (
                    self.withing_board(nr, nc, len(board), len(board[0]))
                    and (nr, nc) not in seen
                    and board[nr][nc] == char
                ):
                    res = recursion(board, nr, nc, word[1:], seen | {(nr, nc)})
                    if res:
                        return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = recursion(board, i, j, word[1:], {(i, j)})
                    if res:
                        return True
        return False


class Solution2:
    def withing_board(self, r, c, m, n):
        return 0 <= r < m and 0 <= c < n

    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(word, r, c, d, seen):
            if len(word) == 0:
                return True
            if word[0] in d[r][c]:
                coords = d[r][c][word[0]]
                for coord in coords:
                    if coord not in seen:
                        res = check(word[1:], coord[0], coord[1], d, seen | {coord})
                        if res:
                            return True
            return False

        m, n = len(board), len(board[0])
        d = [[defaultdict(list) for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):
                for r, c in DIRECTIONS:
                    nr, nc = i + r, j + c
                    if self.withing_board(nr, nc, m, n):
                        d[i][j][board[nr][nc]].append((nr, nc))
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = check(word[1:], i, j, d, {(i, j)})
                    if res:
                        return True
        return False


if __name__ == "__main__":
    inputs = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
        ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"),
    ]
    s = Solution2()
    for board, word in inputs:
        print(s.exist(board, word))

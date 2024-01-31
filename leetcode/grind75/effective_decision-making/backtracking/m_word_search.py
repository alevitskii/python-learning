from collections import defaultdict
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, word, board):
            if len(word) == 0:
                return True
            if not (0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] != word[0]:
                return False
            board[row][col] = "*"
            for row_offset, col_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if dfs(row + row_offset, col + col_offset, word[1:], board):
                    return True
            board[row][col] = word[0]
            return False

        n = len(board)
        m = len(board[0])
        for row in range(n):
            for col in range(m):
                if dfs(row, col, word, board):
                    return True
        return False


if __name__ == "__main__":
    inputs = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
        ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"),
    ]
    s = Solution()
    for board, word in inputs:
        print(s.exist(board, word))

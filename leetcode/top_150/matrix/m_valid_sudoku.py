from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for col in row:
                if col in seen:
                    return False
                if col != ".":
                    seen.add(col)
        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen:
                    return False
                if board[j][i] != ".":
                    seen.add(board[j][i])

        square = [(i, j) for i in range(3) for j in range(3)]
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                seen = set()
                for r, c in square:
                    n = board[i + r][j + c]
                    if n in seen:
                        return False
                    if n != ".":
                        seen.add(n)
        return True


class Solution2:
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))


if __name__ == "__main__":
    inputs = [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    ]
    s = Solution2()
    for board in inputs:
        print(s.isValidSudoku(board))

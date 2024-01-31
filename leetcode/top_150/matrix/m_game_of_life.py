from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def on_board(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        m, n = len(board), len(board[0])
        matrix = [[0] * n for _ in range(m)]
        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = sum([board[i + r][j + c] for r, c in directions if on_board(i + r, j + c)])
                if (board[i][j] and (live < 2 or live > 3)) or (not board[i][j] and live == 3):
                    matrix[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = (board[i][j] + matrix[i][j]) % 2


class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # RC #
        # APPRAOCH : IN-PLACE MANIPULATION #
        #  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0 but we do in increments
        #  and decrements of 2. (table explains)
        #   previous value state change  current state   current value
        #   0              no change     dead            0
        #   1              no change     live            1
        #   0              changed (+2)  live            2
        #   1              changed (-2)  dead            -1

        # TIME COMPLEXITY : O(MxN) #
        # SPACE COMPLEXITY : O(1) #

        def on_board(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])

        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0  # live neighbors count
                for x, y in directions:  # check and count neighbors in all directions
                    if on_board(i + x, j + y) and abs(board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:  # Rule 4
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if board[i][j] > 0 else 0


class Solution3:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])

        # Calculate the number of live neighbors for each cell
        def live_neighbors(i, j):
            directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
            count = 0
            for x, y in directions:
                ni, nj = i + x, j + y
                # Check the least significant bit for current state
                if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] & 1):
                    count += 1
            return count

        # Go through each cell and compute its next state, storing it in the second least significant bit
        for i in range(m):
            for j in range(n):
                neighbors = live_neighbors(i, j)
                if board[i][j] == 1 and (neighbors == 2 or neighbors == 3):
                    board[i][j] |= 2  # Set the second bit to 1
                elif board[i][j] == 0 and neighbors == 3:
                    board[i][j] |= 2  # Set the second bit to 1

        # Update the board to the next state
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  # Shift each cell's value one bit to the right


if __name__ == "__main__":
    inputs = [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[1, 1], [1, 0]]]
    s = Solution3()
    for board in inputs:
        print(s.gameOfLife(board))
        print(board)

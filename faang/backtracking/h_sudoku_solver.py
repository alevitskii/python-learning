def get_box_id(r, c):
    return r // 3 * 3 + c // 3


def is_valid(num, box, row, col):
    return num not in box and num not in row and num not in col


def solve_backtrack(board, boxes, rows, cols, r, c):
    if r == len(board) or c == len(board[0]):
        return True
    if board[r][c] == ".":
        for num in range(1, 10):
            num_val = str(num)
            board[r][c] = num_val
            box_id = get_box_id(r, c)
            if is_valid(num_val, boxes[box_id], rows[r], cols[c]):
                boxes[box_id].add(num_val)
                rows[r].add(num_val)
                cols[c].add(num_val)
                if c == len(board[0]) - 1:
                    if solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                        return True
                else:
                    if solve_backtrack(board, boxes, rows, cols, r, c + 1):
                        return True
                boxes[box_id].remove(num_val)
                rows[r].remove(num_val)
                cols[c].remove(num_val)
            board[r][c] = "."
    else:
        if c == len(board[0]) - 1:
            if solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                return True
        else:
            if solve_backtrack(board, boxes, rows, cols, r, c + 1):
                return True


# T: O(9!**9), S: O(81) ~ O(1)
def solve_sudoku(board):
    n = len(board)
    boxes, rows, cols = [], [], []

    for _ in range(n):
        boxes.append(set())
        rows.append(set())
        cols.append(set())

    for r in range(n):
        for c in range(n):
            if board[r][c] != ".":
                boxes[get_box_id(r, c)].add(board[r][c])
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

    solve_backtrack(board, boxes, rows, cols, 0, 0)


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
        # [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
        #  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
        #  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
        #  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
        #  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
        #  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
        #  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
        #  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
        #  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
        [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ],
    ]
    for board in inputs:
        solve_sudoku(board)
        print(board)

from math import inf

DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left


# T: O(n), S: O(n)
def walls_and_gates_bfs(matrix):
    queue = []
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 0:
                queue.append([row_idx, col_idx, 0])

    while queue:
        row, col, length = queue.pop(0)
        for row_shift, col_shift in DIRECTIONS:
            new_row, new_col = row + row_shift, col + col_shift
            if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
                continue
            if matrix[new_row][new_col] == inf or matrix[new_row][new_col] > length + 1:
                matrix[new_row][new_col] = length + 1
                queue.append([new_row, new_col, length + 1])


def dfs(matrix, row, col, length):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] < length:
        return
    matrix[row][col] = length
    for row_shift, col_shift in DIRECTIONS:
        dfs(matrix, row + row_shift, col + col_shift, length + 1)


# T: O(n), S: O(n)
def walls_and_gates_dfs(matrix):
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 0:
                dfs(matrix, row_idx, col_idx, 0)


if __name__ == "__main__":
    inputs = [
        [[inf, -1, 0, inf], [inf, inf, inf, -1], [inf, -1, inf, -1], [0, -1, inf, inf]],
        [[inf, -1, 0, inf], [-1, inf, inf, -1], [inf, -1, inf, -1], [0, -1, inf, inf]],
        [],
        [[]],
    ]
    for matrix in inputs:
        # walls_and_gates_bfs(matrix)
        walls_and_gates_dfs(matrix)
        print(matrix)

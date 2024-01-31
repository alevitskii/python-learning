DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left


def dfs(matrix, row, col, seen, values):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
        return
    values.append(matrix[row][col])
    seen[row][col] = True
    for row_shift, col_shift in DIRECTIONS:
        dfs(matrix, row + row_shift, col + col_shift, seen, values)


# T: O(n), S: O(n)
def traversal_dfs(matrix):
    seen = [len(matrix[0]) * [False] for _ in range(len(matrix))]
    values = []
    dfs(matrix, 0, 0, seen, values)
    return values


# T: O(n), S: O(n)
def traversal_bfs(matrix):
    seen = [len(matrix[0]) * [False] for _ in range(len(matrix))]
    values = []
    queue = [[0, 0]]
    while queue:
        row, col = queue.pop(0)
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or seen[row][col]:
            continue
        values.append(matrix[row][col])
        seen[row][col] = True
        for row_shift, col_shift in DIRECTIONS:
            queue.append([row + row_shift, col + col_shift])
    return values


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    print(traversal_dfs(matrix))
    print(traversal_bfs(matrix))

DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left


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


def number_of_islands(matrix):
    seen = [len(matrix[0]) * [False] for _ in range(len(matrix))]
    islands = 0
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 1 and not seen[row_idx][col_idx]:
                queue = [[row_idx, col_idx]]
                while queue:
                    row, col = queue.pop(0)
                    if (
                        row < 0
                        or row >= len(matrix)
                        or col < 0
                        or col >= len(matrix[0])
                        or seen[row][col]
                        or matrix[row][col] != 1
                    ):
                        continue
                    seen[row][col] = True
                    for row_shift, col_shift in DIRECTIONS:
                        queue.append([row + row_shift, col + col_shift])
                islands += 1
    return islands


# T: O(2*m*n) ~ O(m*n), S: O(max(m,n))
def number_of_islands_2(matrix):
    count = 0
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 1:
                count += 1
                matrix[row_idx][col_idx] = 0
                queue = [[row_idx, col_idx]]
                while queue:
                    row, col = queue.pop(0)
                    for row_shift, col_shift in DIRECTIONS:
                        next_row = row + row_shift
                        next_col = col + col_shift
                        if (
                            next_row < 0
                            or next_row >= len(matrix)
                            or next_col < 0
                            or next_col >= len(matrix[0])
                            or matrix[next_row][next_col] != 1
                        ):
                            continue
                        queue.append([next_row, next_col])
                        matrix[next_row][next_col] = 0
    return count


# DFS. T: O(m*n), S: O(m*n)


if __name__ == "__main__":
    inputs = [
        [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 0, 0, 1, 1]],  # 2
        [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 0, 1]],  # 7
        [],  # 0
        [[], []],  # 0
    ]
    for matrix in inputs:
        print(number_of_islands(matrix))
        print(number_of_islands_2(matrix))

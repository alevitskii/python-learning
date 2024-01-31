DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up  # right  # down  # left


def rotting_oranges(matrix):
    fresh = 0
    minutes = 0
    rotten = []
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 1:
                fresh += 1
            elif matrix[row_idx][col_idx] == 2:
                rotten.append([row_idx, col_idx])
    while rotten:
        count, length = 0, len(rotten)
        while count < length:
            count += 1
            row, col = rotten.pop(0)
            for row_shift, col_shift in DIRECTIONS:
                new_row, new_col = row + row_shift, col + col_shift
                if (
                    new_row < 0
                    or new_row >= len(matrix)
                    or new_col < 0
                    or new_col >= len(matrix[0])
                    or matrix[new_row][new_col] in {0, 2}
                ):
                    continue
                matrix[new_row][new_col] = 2
                fresh -= 1
                rotten.append([new_row, new_col])
        if len(rotten) == 0:
            break
        minutes += 1
    return -1 if fresh > 0 else minutes


# T: O(n), S: O(n)
def rotting_oranges_2(matrix):
    fresh = 0
    rotten = []
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            if matrix[row_idx][col_idx] == 1:
                fresh += 1
            elif matrix[row_idx][col_idx] == 2:
                rotten.append([row_idx, col_idx])
    current_queue_size = len(rotten)
    minutes = 0
    while len(rotten) > 0:
        if current_queue_size == 0:
            minutes += 1
            current_queue_size = len(rotten)
        row, col = rotten.pop(0)
        current_queue_size -= 1
        for row_shift, col_shift in DIRECTIONS:
            new_row, new_col = row + row_shift, col + col_shift
            if (
                new_row < 0
                or new_row >= len(matrix)
                or new_col < 0
                or new_col >= len(matrix[0])
                or matrix[new_row][new_col] in {0, 2}
            ):
                continue
            matrix[new_row][new_col] = 2
            fresh -= 1
            rotten.append([new_row, new_col])
    return -1 if fresh > 0 else minutes


if __name__ == "__main__":
    inputs = [
        [[2, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 1, 0, 0, 1]],  # 7
        [[1, 1, 0, 0, 0], [2, 1, 0, 0, 0], [0, 0, 0, 1, 2], [0, 1, 0, 0, 1]],  # -1
        [],  # 0
        [[], []],  # 0
    ]
    for matrix in inputs:
        print(rotting_oranges(matrix))
        print(rotting_oranges_2(matrix))

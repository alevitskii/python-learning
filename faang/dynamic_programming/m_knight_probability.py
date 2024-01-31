DIRECTIONS = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]


def knight_probability_top_down(n, k, r, c):
    def dfs(n, k, r, c, dp):
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0
        if k == 0:
            return 1
        if (k, r, c) in dp:
            return dp[(k, r, c)]
        dp[(k, r, c)] = (
            sum([dfs(n, k - 1, r + row_shift, c + col_shift, dp) for row_shift, col_shift in DIRECTIONS]) / 8
        )
        return dp[(k, r, c)]

    return dfs(n, k, r, c, {})


# T: O(8**k), O(8**k)
def knight_probability_recursive(n, k, r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return 0
    if k == 0:
        return 1
    return (
        sum(
            [
                knight_probability_recursive(n, k - 1, r + row_shift, c + col_shift)
                for row_shift, col_shift in DIRECTIONS
            ]
        )
        / 8
    )


# T: O(k*n**2), S: O(k*n**2)
def knight_probability_top_down_memo(n, k, r, c):
    dp = [[[None] * n for __ in range(n)] for _ in range(k + 1)]

    def recurse(n, k, r, c, dp):
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0
        if k == 0:
            return 1
        if dp[k][r][c] is not None:
            return dp[k][r][c]
        res = 0
        for row_shift, col_shift in DIRECTIONS:
            res += recurse(n, k - 1, r + row_shift, c + col_shift, dp) / 8
        dp[k][r][c] = res
        return dp[k][r][c]

    return recurse(n, k, r, c, dp)


# T: O(k*n**2), S: O(k*n**2)
def knight_probability_bottom_up(n, k, r, c):
    if n == 0:
        return 0
    if k == 0:
        return 1

    dp = [[[0] * n for __ in range(n)] for _ in range(k + 1)]
    dp[0][r][c] = 1
    for step in range(1, k + 1):
        for row in range(n):
            for col in range(n):
                for row_shift, col_shift in DIRECTIONS:
                    prev_row = row + row_shift
                    prev_col = col + col_shift
                    if prev_row >= 0 and prev_row < n and prev_col >= 0 and prev_col < n:
                        dp[step][row][col] += dp[step - 1][prev_row][prev_col] / 8
    return sum([sum(row) for row in dp[k]])


# T: O(k*n**2), S: O(n**2)
def knight_probability_bottom_up_opt(n, k, r, c):
    if n == 0:
        return 0
    if k == 0:
        return 1

    prev_dp = [[0] * n for _ in range(n)]
    curr_dp = [[0] * n for _ in range(n)]
    prev_dp[r][c] = 1
    for _ in range(1, k + 1):
        for row in range(n):
            for col in range(n):
                for row_shift, col_shift in DIRECTIONS:
                    prev_row = row + row_shift
                    prev_col = col + col_shift
                    if prev_row >= 0 and prev_row < n and prev_col >= 0 and prev_col < n:
                        curr_dp[row][col] += prev_dp[prev_row][prev_col] / 8
        prev_dp = curr_dp
        curr_dp = [[0] * n for _ in range(n)]
    return sum([sum(row) for row in prev_dp])


if __name__ == "__main__":
    inputs = [
        [6, 3, 2, 2],
        [8, 30, 6, 4],
        # [0, 2, 1, 2],  # 0
        # [2, 3, 1, 1],  # 0
        # [2, 0, 1, 1]  # 1
    ]
    for args in inputs:
        print(knight_probability_top_down(*args))
        # print(knight_probability_recursive(*args))
        # print(knight_probability_top_down_memo(*args))
        # print(knight_probability_bottom_up(*args))
        # print(knight_probability_bottom_up_opt(*args))

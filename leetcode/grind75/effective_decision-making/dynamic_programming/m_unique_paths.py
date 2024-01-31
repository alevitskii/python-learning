class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        for c in range(n):
            memo[(0, c)] = 1
        for r in range(m):
            memo[(r, 0)] = 1
        for r in range(1, m):
            for c in range(1, n):
                memo[(r, c)] = memo[(r - 1, c)] + memo[(r, c - 1)]
        return memo[(m - 1, n - 1)]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
        return grid[m - 1][n - 1]


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        rolling_array = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                rolling_array[col] += rolling_array[col - 1]
        return rolling_array[-1]


class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        # C(h, k) = h! / (k! * (h-k)!)
        # h = m-1 + n-1
        # k = n-1 (why?)
        result = 1
        for i in range(1, n):
            result *= m - 1 + i
            result //= i
        return result


if __name__ == "__main__":
    inputs = [
        (3, 7),
        (3, 2),
        (1, 1),
    ]

    s = Solution2()
    for m, n in inputs:
        print(s.uniquePaths(m, n))

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]

        dp = {}
        return dfs(0, 0)


if __name__ == "__main__":
    inputs = [
        ("rabbbit", "rabbit"),
        ("babgbag", "bag"),
    ]
    s = Solution()
    for string, t in inputs:
        print(s.numDistinct(string, t))

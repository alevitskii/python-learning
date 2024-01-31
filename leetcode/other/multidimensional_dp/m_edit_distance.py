class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            if i == len(word1):
                return len(word2[j:])
            if j == len(word2):
                return len(word1[i:])
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            return dp[(i, j)]

        dp = {}
        return dfs(0, 0)


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        dp[len(word1)] = list(range(len(word2), -1, -1))
        for i in range(len(word1) + 1):
            dp[i][-1] = len(word1) - i
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]


if __name__ == "__main__":
    inputs = [
        ("horse", "ros"),
        ("intention", "execution"),
    ]
    s = Solution2()
    for word1, word2 in inputs:
        print(s.minDistance(word1, word2))

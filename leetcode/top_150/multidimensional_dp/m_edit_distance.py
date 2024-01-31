class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word2) + 1))
        cur = [0] * (len(word2) + 1)
        for i in range(1, len(word1) + 1):
            cur[0] = i
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = min(prev[j - 1] + 1, prev[j] + 1, cur[j - 1] + 1)
            prev = cur
            cur = [0] * (len(word2) + 1)
        return prev[-1]


if __name__ == "__main__":
    inputs = [
        ("horse", "ros"),
        ("intention", "execution"),
    ]
    s = Solution()
    for word1, word2 in inputs:
        print(s.minDistance(word1, word2))

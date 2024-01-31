class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for c1 in range(l1 - 1, -1, -1):
            for c2 in range(l2 - 1, -1, -1):
                if text1[c1] == text2[c2]:
                    dp[c1][c2] = dp[c1 + 1][c2 + 1] + 1
                else:
                    dp[c1][c2] = max(dp[c1 + 1][c2], dp[c1][c2 + 1])
        return dp[0][0]


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        prev = [0] * (l2 + 1)
        for c1 in range(l1 - 1, -1, -1):
            curr = [0] * (l2 + 1)
            for c2 in range(l2 - 1, -1, -1):
                if text1[c1] == text2[c2]:
                    curr[c2] = prev[c2 + 1] + 1
                else:
                    curr[c2] = max(prev[c2], curr[c2 + 1])
            prev = curr
        return prev[0]


class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(text1, text2, i, j, dp):
            if i == len(text1) or j == len(text2):
                return 0
            elif dp[i][j] == -1:
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dfs(text1, text2, i + 1, j + 1, dp)
                else:
                    dp[i][j] = max(dfs(text1, text2, i + 1, j, dp), dfs(text1, text2, i, j + 1, dp))
            return dp[i][j]

        n = len(text1)
        m = len(text2)
        dp = [[-1 for x in range(m)] for y in range(n)]
        return dfs(text1, text2, 0, 0, dp)


if __name__ == "__main__":
    inputs = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
    ]
    s = Solution3()
    for text1, text2 in inputs:
        print(s.longestCommonSubsequence(text1, text2))

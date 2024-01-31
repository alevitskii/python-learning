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


if __name__ == "__main__":
    inputs = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
    ]
    s = Solution()
    for text1, text2 in inputs:
        print(s.longestCommonSubsequence(text1, text2))

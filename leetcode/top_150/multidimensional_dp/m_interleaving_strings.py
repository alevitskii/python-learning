class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def rec(s1p, s2p, s3p):
            if s1p == len(s1) and s2p == len(s2) and s3p == len(s3):
                return True
            if (s1p, s2p) in memo:
                return memo[(s1p, s2p)]
            if s1p < len(s1) and s2p < len(s2) and s3p < len(s3) and s1[s1p] == s2[s2p] == s3[s3p]:
                memo[(s1p, s2p)] = rec(s1p + 1, s2p, s3p + 1) or rec(s1p, s2p + 1, s3p + 1)
                return memo[(s1p, s2p)]
            elif s1p < len(s1) and s3p < len(s3) and s1[s1p] == s3[s3p]:
                memo[(s1p, s2p)] = rec(s1p + 1, s2p, s3p + 1)
                return memo[(s1p, s2p)]
            elif s2p < len(s2) and s3p < len(s3) and s2[s2p] == s3[s3p]:
                memo[(s1p, s2p)] = rec(s1p, s2p + 1, s3p + 1)
                return memo[(s1p, s2p)]
            return False

        memo = {}
        return rec(0, 0, 0)


class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        dp[0][0] = True
        for c in range(1, len(dp[0])):
            if s1[c - 1] == s3[c - 1]:
                dp[0][c] = dp[0][c - 1]
        for r in range(1, len(dp)):
            if s2[r - 1] == s3[r - 1]:
                dp[r][0] = dp[r - 1][0]
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                dp[r][c] = (dp[r - 1][c] and s2[r - 1] == s3[r + c - 1]) or (
                    dp[r][c - 1] and s1[c - 1] == s3[r + c - 1]
                )
        return dp[len(s2)][len(s1)]


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, k = len(s1), len(s2), len(s3)
        if m + n != k:
            return False
        if m < n:
            return self.isInterleave(s2, s1, s3)
        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[n]


def main() -> None:
    inputs = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabccaabccaabcc", "dbbcadbbcadbbcadbbca", "aadbbcbcacaadbbcbcacaadbbcbcacaadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", ""),
    ]
    s = Solution()
    for s1, s2, s3 in inputs:
        print(s.isInterleave(s1, s2, s3))


if __name__ == "__main__":
    main()

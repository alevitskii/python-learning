class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False
            return False

        dp = {}
        return dfs(0, 0)


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        if not s1 or not s2:
            return s1 == s3 or s2 == s3
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        for r in range(len(s1), -1, -1):
            for c in range(len(s2), -1, -1):
                if r < len(s1) and s1[r] == s3[r + c] and dp[r + 1][c]:
                    dp[r][c] = True
                if c < len(s2) and s2[c] == s3[r + c] and dp[r][c + 1]:
                    dp[r][c] = True
        return dp[0][0]


def main() -> None:
    inputs = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabccaabccaabcc", "dbbcadbbcadbbcadbbca", "aadbbcbcacaadbbcbcacaadbbcbcacaadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", ""),
        ("a", "c", "cc"),
    ]
    s = Solution2()
    for s1, s2, s3 in inputs:
        print(s.isInterleave(s1, s2, s3))


if __name__ == "__main__":
    main()

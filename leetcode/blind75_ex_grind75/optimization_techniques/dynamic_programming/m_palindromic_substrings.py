class Solution:
    def countSubstrings(self, s: str) -> str:
        def expand(left, right):
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt

        count = 0
        for i in range(len(s)):
            count += expand(i, i) + expand(i, i + 1)
        return count


class Solution2:
    def countSubstrings(self, s: str) -> str:
        count = 0
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            count += dp[i][i + 1]
        for length in range(3, len(s) + 1):
            i = 0
            for j in range(length - 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                count += dp[i][j]
                i += 1
        return count


if __name__ == "__main__":
    inputs = [
        "abc",
        "aaa",
        "a",
    ]
    s = Solution()
    for string in inputs:
        print(s.countSubstrings(string))

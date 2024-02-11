# https://en.wikipedia.org/wiki/Longest_palindromic_substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 1
        max_str = s[0]
        s = "#" + "#".join(s) + "#"
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i - dp[i] : i + dp[i] + 1].replace("#", "")
        return max_str


def main() -> None:
    inputs = [
        # "babad",
        # "cbbd",
        "peeweep",
    ]
    s = Solution()
    for string in inputs:
        print(s.longestPalindrome(string))


if __name__ == "__main__":
    main()

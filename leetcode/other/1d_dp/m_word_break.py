from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def check(i, words, dp):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            for word in words:
                if s[i : i + len(word)] == word and check(i + len(word), words, dp):
                    dp[i] = True
                    return True
            dp[i] = False
            return False

        return check(0, wordDict, {})


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                dp[i] = s[i : i + len(word)] == word and (i + len(word) >= len(dp) or dp[i + len(word)])
                if dp[i]:
                    break
        return dp[0]


class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]


def main() -> None:
    inputs = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("a", ["b"]),
    ]
    s = Solution3()
    for string, wordDict in inputs:
        print(s.wordBreak(string, wordDict))


if __name__ == "__main__":
    main()

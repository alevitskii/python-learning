from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def check(string, words, dp):
            if string in dp:
                return dp[string]
            if not string:
                return True
            for word in words:
                if string.startswith(word) and check(string[len(word) :], words, dp):
                    dp[string] = True
                    return True
            dp[string] = False
            return False

        return check(s, wordDict, {})


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == "__main__":
    inputs = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("a", ["b"]),
    ]
    s = Solution()
    for string, wordDict in inputs:
        print(s.wordBreak(string, wordDict))

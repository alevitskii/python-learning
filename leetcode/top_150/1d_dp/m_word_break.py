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


def main() -> None:
    inputs = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("a", ["b"]),
    ]
    s = Solution()
    for string, wordDict in inputs:
        print(s.wordBreak(string, wordDict))


if __name__ == "__main__":
    main()

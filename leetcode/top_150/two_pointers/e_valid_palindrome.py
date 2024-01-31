import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]+", "", s).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]+", "", s).lower()
        return s == s[::-1]


if __name__ == "__main__":
    inputs = ["A man, a plan, a canal: Panama", "race a car", ""]
    s = Solution()
    for string in inputs:
        print(s.isPalindrome(string))

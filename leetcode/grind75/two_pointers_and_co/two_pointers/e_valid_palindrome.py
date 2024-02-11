import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "aquickbrownfoxjumpsoverthelazydog0123456789"

        left_shift = 0
        right_shift = len(s) - 1
        s = s.lower()
        is_p = True

        if not s:
            return True

        while left_shift < right_shift:
            if s[left_shift] not in t:
                left_shift += 1
                continue
            if s[right_shift] not in t:
                right_shift -= 1
                continue
            if s[left_shift] != s[right_shift]:
                is_p = False
                break
            else:
                left_shift += 1
                right_shift -= 1

        return is_p


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^0-9a-zA-Z]+", "", s).lower()
        return s == s[::-1]


def main() -> None:
    inputs = ["A man, a plan, a canal: Panama", "race a car", " "]

    s = Solution2()
    for string in inputs:
        print(s.isPalindrome(string))


if __name__ == "__main__":
    main()

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) <= 1:
            return s
        max_str = s[0]
        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str


def main() -> None:
    inputs = [
        "babad",
        "cbbd",
    ]
    s = Solution()
    for string in inputs:
        print(s.longestPalindrome(string))


if __name__ == "__main__":
    main()

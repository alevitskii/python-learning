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


def main() -> None:
    inputs = [
        "abc",
        "aaa",
        "a",
    ]
    s = Solution()
    for string in inputs:
        print(s.countSubstrings(string))


if __name__ == "__main__":
    main()

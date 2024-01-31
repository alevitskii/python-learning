class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hidx = 0
        haylength = len(haystack) - len(needle) + 1
        while hidx < haylength:
            if haystack[hidx] == needle[0]:
                for nidx in range(1, len(needle)):
                    if haystack[hidx + nidx] != needle[nidx]:
                        break
                else:
                    return hidx
            hidx += 1
        return -1


if __name__ == "__main__":
    inputs = [
        ("sadbutsad", "sad"),
        ("leetcode", "code"),
        ("leetcode", "etc"),
        ("leetcode", "eee"),
    ]
    s = Solution()
    for haystack, needle in inputs:
        print(s.strStr(haystack, needle))

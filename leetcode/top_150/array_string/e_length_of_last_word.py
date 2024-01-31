class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        length = 0
        while idx >= 0:
            if s[idx] == " ":
                if length > 0:
                    return length
            else:
                length += 1
            idx -= 1
        return length


if __name__ == "__main__":
    inputs = [
        "HelloWorld",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
    ]
    s = Solution()
    for string in inputs:
        print(s.lengthOfLastWord(string))

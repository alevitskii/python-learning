from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or mapping[c] != stack.pop():
                return False
        return not stack


if __name__ == "__main__":
    inputs = ["()", "()[]{}", "(]", "]"]
    s = Solution()
    for string in inputs:
        print(s.isValid(string))

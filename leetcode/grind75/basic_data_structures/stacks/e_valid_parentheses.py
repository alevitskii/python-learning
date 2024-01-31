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


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if stack:
                    popped_element = stack.pop()
                else:
                    popped_element = "*"

                if hashmap[char] != popped_element:
                    return False
        return not stack


if __name__ == "__main__":
    inputs = ["()", "()[]{}", "(]"]
    s = Solution2()
    for string in inputs:
        print(s.isValid(string))

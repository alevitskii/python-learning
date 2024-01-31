class Solution:
    def reverseWords(self, s: str) -> str:
        s: list = list(s)
        idx = 0
        insert_idx = 0
        while idx < len(s):
            if s[idx] != " ":
                s[insert_idx] = s[idx]
                idx += 1
                insert_idx += 1
                if idx < len(s) and s[idx] == " ":
                    s[insert_idx] = " "
                    insert_idx += 1
                    idx += 1
            else:
                idx += 1
        while idx > insert_idx or s[-1] == " ":
            s.pop()
            idx -= 1
        s.reverse()

        start_idx = 0
        idx = 0
        while idx < len(s):
            if s[idx] == " ":
                left, right = start_idx, idx - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                idx += 1
                start_idx = idx
            else:
                idx += 1
        left, right = start_idx, idx - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


class Solution2:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    inputs = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
    ]
    s = Solution2()
    for string in inputs:
        print(s.reverseWords(string))

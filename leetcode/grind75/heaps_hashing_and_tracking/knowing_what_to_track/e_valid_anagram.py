class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c not in d:
                return False
            d[c] -= 1
            if d[c] == 0:
                del d[c]
        return not d


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = {}
        for i in s:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        for i in t:
            if i in table:
                table[i] -= 1
            else:
                return False
        for key in table:
            if table[key] != 0:
                return False
        return True


if __name__ == "__main__":
    inputs = [
        ("anagram", "nagaram"),
        ("rat", "car"),
    ]
    s = Solution2()
    for string, q in inputs:
        print(s.isAnagram(string, q))

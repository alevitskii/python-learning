from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in ransomNote:
            d[c] = d.get(c, 0) + 1
        for c in magazine:
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]
                if not d:
                    return True
        return False


class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        rn, mg = Counter(ransomNote), Counter(magazine)
        return rn & mg == rn


if __name__ == "__main__":
    inputs = [
        ("a", "b"),
        ("aa", "ab"),
        ("aa", "aab"),
    ]
    s = Solution2()
    for ransomNote, magazine in inputs:
        print(s.canConstruct(ransomNote, magazine))

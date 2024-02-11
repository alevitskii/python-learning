from collections import Counter, defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for w in ransomNote:
            if w not in d:
                d[w] = 0
            d[w] += 1
        for w in magazine:
            if w in d:
                d[w] -= 1
                if d[w] == 0:
                    del d[w]
                if not d:
                    return True
        return False


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn, mg = Counter(ransomNote), Counter(magazine)
        return rn & mg == rn


class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = defaultdict(int)
        for char in magazine:
            frequency[char] += 1
        for char in ransomNote:
            if not frequency[char]:
                return False
            frequency[char] -= 1
        return True


def main() -> None:
    inputs = [
        ("a", "a"),
        ("aa", "ab"),
        ("aa", "aab"),
    ]
    s = Solution3()
    for ransomNote, magazine in inputs:
        print(s.canConstruct(ransomNote, magazine))


if __name__ == "__main__":
    main()

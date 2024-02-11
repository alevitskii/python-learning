class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        idx = 0
        d = {}
        seen = set()
        while idx < len(s):
            if s[idx] in d:
                if d[s[idx]] != t[idx]:
                    return False
            else:
                if t[idx] in seen:
                    return False
                seen.add(t[idx])
                d[s[idx]] = t[idx]
            idx += 1
        return True


def main() -> None:
    inputs = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
    ]
    s = Solution()
    for string, t in inputs:
        print(s.isIsomorphic(string, t))


if __name__ == "__main__":
    main()

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


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # [*map(s.index, s)] == [*map(t.index, t)]
        return list(map(s.index, s)) == list(map(t.index, t))


def main() -> None:
    inputs = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
        ("qadc", "babt"),
    ]
    s = Solution2()
    for string, another_string in inputs:
        print(s.isIsomorphic(string, another_string))


if __name__ == "__main__":
    main()

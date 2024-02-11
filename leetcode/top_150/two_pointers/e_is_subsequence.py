class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx, tidx = 0, 0
        while sidx < len(s):
            for i in range(tidx, len(t)):
                if s[sidx] == t[i]:
                    tidx = i + 1
                    sidx += 1
                    break
            else:
                return False
        return True


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        nxt = [{} for _ in range(len(t) + 1)]
        for i in range(len(t) - 1, -1, -1):
            nxt[i] = nxt[i + 1].copy()
            nxt[i][t[i]] = i + 1
        i = 0
        for c in s:
            if c in nxt[i]:
                i = nxt[i][c]
            else:
                return False
        return True


def main() -> None:
    inputs = [
        ("abc", "ahbgdc"),
        ("aa", "ahbaqc"),
    ]
    s = Solution3()
    for sub, string in inputs:
        print(s.isSubsequence(sub, string))


if __name__ == "__main__":
    main()

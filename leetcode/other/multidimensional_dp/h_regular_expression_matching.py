class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s) and j == len(p):
                dp[(i, j)] = False
            elif i == len(s):
                while j < len(p):
                    if j + 1 < len(p) and p[j + 1] == "*":
                        j += 2
                        continue
                    dp[(i, j)] = False
                    break
                else:
                    dp[(i, j)] = True
            elif j + 1 < len(p) and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    dp[(i, j)] = dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    dp[(i, j)] = dfs(i, j + 2)
            elif p[j] == ".":
                dp[(i, j)] = dfs(i + 1, j + 1)
            elif s[i] == p[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]

        dp = {}
        return dfs(0, 0)


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return dp[(i, j)]

        dp = {}
        return dfs(0, 0)


if __name__ == "__main__":
    inputs = [
        ("aa", "a"),
        ("aa", "a*"),
        ("ab", ".*"),
        ("aaa", "a*a"),
    ]
    s = Solution2()
    for string, p in inputs:
        print(s.isMatch(string, p))

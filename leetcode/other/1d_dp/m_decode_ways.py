class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res

        dp = {len(s): 1}
        return dfs(0)


class Solution2:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
        return dp[0]


class Solution3:
    def numDecodings(self, s: str) -> int:
        curr, oneback, twoback = 0, 1, 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = oneback
                if i + 1 < len(s) and int(s[i] + s[i + 1]) <= 26:
                    curr += twoback
            twoback = oneback
            oneback = curr
        return curr


class Solution4:
    def numDecodings(self, s: str) -> int:
        str_len = len(s)
        dp = [0] * (str_len + 1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1
        else:
            return 0
        for i in range(2, str_len + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]
        return dp[str_len]


def main() -> None:
    inputs = [
        "12",
        "226",
        "06",
        "11106",
    ]
    s = Solution3()
    for string in inputs:
        print(s.numDecodings(string))


if __name__ == "__main__":
    main()

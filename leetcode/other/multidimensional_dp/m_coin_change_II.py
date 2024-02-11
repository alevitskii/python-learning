from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        cache = {}
        return dfs(0, 0)


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]


class Solution3:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            next_dp = [0] * (amount + 1)
            next_dp[0] = 1
            for a in range(1, amount + 1):
                next_dp[a] = dp[a]
                if a - coins[i] >= 0:
                    next_dp[a] += next_dp[a - coins[i]]
            dp = next_dp
        return dp[amount]


def main() -> None:
    inputs = [
        (5, [1, 2, 5]),
        (3, [2]),
        (10, [10]),
    ]
    s = Solution2()
    for amount, coins in inputs:
        print(s.change(amount, coins))


if __name__ == "__main__":
    main()

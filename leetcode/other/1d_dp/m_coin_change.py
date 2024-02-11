from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(amount):
            if amount < 0:
                return float("inf")
            if amount in dp:
                return dp[amount]
            if amount == 0:
                return 0
            dp[amount] = float("inf")
            for coin in coins:
                dp[amount] = min(dp[amount], 1 + dfs(amount - coin))
            return dp[amount]

        dp = {}
        res = dfs(amount)
        return res if res != float("inf") else -1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float("inf") else -1


def main() -> None:
    inputs = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
    ]
    s = Solution2()
    for coins, amount in inputs:
        print(s.coinChange(coins, amount))


if __name__ == "__main__":
    main()

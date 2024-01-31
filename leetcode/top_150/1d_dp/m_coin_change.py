from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == inf else dp[-1]


if __name__ == "__main__":
    inputs = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
    ]
    s = Solution()
    for coins, amount in inputs:
        print(s.coinChange(coins, amount))

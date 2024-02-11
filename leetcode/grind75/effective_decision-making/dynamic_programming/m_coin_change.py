from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i - coin] + 1

        return -1 if dp[-1] == float("inf") else dp[-1]


class Solution2:
    def calculate_minimum_coins(self, coins, rem, counter):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if counter[rem - 1] != float("inf"):
            return counter[rem - 1]
        minimum = float("inf")

        for s in coins:
            result = self.calculate_minimum_coins(coins, rem - s, counter)
            if result >= 0 and result < minimum:
                minimum = 1 + result
        counter[rem - 1] = minimum if minimum != float("inf") else -1
        return counter[rem - 1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        return self.calculate_minimum_coins(coins, amount, [float("inf")] * amount)


class Solution3:
    def min_ignore_none(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        for i in range(1, amount + 1):
            for coin in coins:
                subproblem = i - coin
                if subproblem < 0:
                    continue
                memo[i] = self.min_ignore_none(memo.get(i), memo.get(subproblem, float("inf")) + 1)
        return memo[amount] if memo[amount] != float("inf") else -1


def main() -> None:
    inputs = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0),
    ]

    s = Solution3()
    for coins, amount in inputs:
        print(s.coinChange(coins, amount))


if __name__ == "__main__":
    main()

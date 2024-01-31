from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        dp = {}
        return dfs(0, True)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # initialization
        cool_down, sell, hold = 0, -float("inf"), -float("inf")
        for stock_price_of_Day_i in prices:
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            # Max profit of cooldown on Day i comes from either cool down of Day_i-1,
            # or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)


if __name__ == "__main__":
    inputs = [
        [1, 2, 3, 0, 2],
        [1],
    ]
    s = Solution2()
    for prices in inputs:
        print(s.maxProfit(prices))

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx = 1
        min_price = prices[0]
        max_profit = 0
        while idx < len(prices):
            if prices[idx] < prices[idx - 1]:
                max_profit += prices[idx - 1] - min_price
                min_price = prices[idx]
            idx += 1
        return max_profit + prices[idx - 1] - min_price


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit_from_price_gain = 0
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]:
                profit_from_price_gain += prices[idx + 1] - prices[idx]
        return profit_from_price_gain


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float("inf"), 0
        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            # either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)
            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)
        # maximum profit must be in not-hold state
        return cur_not_hold


def main() -> None:
    inputs = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
        [1, 7, 5, 3, 6, 4],
        [2, 1, 2, 1, 0, 1, 2],
        [2],
        [0, 2],
        [4, 3, 5, 1, 7, 9, 6, 8],
    ]
    s = Solution()
    for prices in inputs:
        print(s.maxProfit(prices))


if __name__ == "__main__":
    main()

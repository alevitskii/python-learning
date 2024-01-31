from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lesser = prices[0]
        for i in prices[1:]:
            if i - lesser > profit:
                profit = i - lesser
            elif lesser > i:
                lesser = i
        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        current_min, max_profit = prices[0], 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - current_min)
            current_min = min(current_min, prices[i])
        return max_profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxprofit = 0
        while sell < len(prices):
            currentprofit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maxprofit = max(currentprofit, maxprofit)
            else:
                buy = sell
            sell += 1
        return maxprofit


if __name__ == "__main__":
    inputs = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
    ]
    s = Solution()
    for prices in inputs:
        print(s.maxProfit(prices))

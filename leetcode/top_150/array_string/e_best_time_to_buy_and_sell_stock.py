from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min, max_profit = prices[0], 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - current_min)
            current_min = min(current_min, prices[i])
        return max_profit


if __name__ == "__main__":
    inputs = [[7, 1, 5, 3, 6, 4], [1, 7, 5, 3, 6, 4], [7, 6, 4, 3, 1], [1, 2, 3, 4, 5, 6], [2, 1, 2, 1, 0, 1, 2]]
    s = Solution()
    for prices in inputs:
        print(s.maxProfit(prices))

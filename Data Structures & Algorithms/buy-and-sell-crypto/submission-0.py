class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        if len(prices) < 2:
            return 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > max_profit:
                max_profit = profit
            if prices[r] < prices[l]:
                l = r
        return max_profit
        
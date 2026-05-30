class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0

        for i in range(1,len(prices)):
            profit = prices[i] - prices[left]
            if profit > maxProfit:
                maxProfit = profit
            if prices[i] < prices[left]:
                left = i
        return maxProfit
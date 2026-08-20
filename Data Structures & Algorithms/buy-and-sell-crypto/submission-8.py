class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        profit = 0
        while p2 < len(prices):
            curr = prices[p2] - prices[p1]
            profit = max(profit, curr)
            if prices[p1] > prices[p2]:
                p1 = p2
                p2 = p1 + 1
            else:
                p2 += 1
        return profit
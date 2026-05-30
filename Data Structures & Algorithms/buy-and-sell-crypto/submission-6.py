class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitToReturn = 0
        buyPriceIndex = 0
        sellPriceIndex = 1
        while sellPriceIndex < len(prices):
            sellPrice = prices[sellPriceIndex]
            buyPrice = prices[buyPriceIndex]
            profit =  sellPrice - buyPrice
            maxProfitToReturn = max(maxProfitToReturn, profit)
            if sellPrice < buyPrice:
                buyPriceIndex = sellPriceIndex
            sellPriceIndex += 1

        return maxProfitToReturn
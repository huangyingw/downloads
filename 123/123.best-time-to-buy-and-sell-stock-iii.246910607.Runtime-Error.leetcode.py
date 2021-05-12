class Solution(object):
    def maxProfit(self, prices):
        preProfit = [0 for _ in range(len(prices))]
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i - 1])
            preProfit[i] = max(preProfit[i - 1], prices[i] - minPrice)
        maxPrice = prices[-1]
        maxProfit = preProfit[-1]
        for i in range(len(prices) - 2, 0, -1):
            maxPrice = max(maxPrice, prices[i])
            maxProfit = max(maxProfit, preProfit[i - 1] + maxPrice - prices[i])
        return maxProfit


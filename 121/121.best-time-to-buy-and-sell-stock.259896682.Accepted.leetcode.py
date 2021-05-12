class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxProfit, low = 0, prices[0]
        for i in range(1, len(prices)):
            low = min(prices[i], low)
            maxProfit = max(prices[i] - low, maxProfit)
        return maxProfit


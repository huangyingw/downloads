class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxProfit, low = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                maxProfit = max(prices[i] - low, maxProfit)
        return maxProfit


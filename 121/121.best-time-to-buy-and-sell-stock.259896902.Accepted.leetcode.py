class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxProfit, minPrice = 0, prices[0]
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)
        return maxProfit


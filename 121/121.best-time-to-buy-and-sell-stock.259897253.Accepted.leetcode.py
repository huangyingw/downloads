class Solution(object):
    def maxProfit(self, prices):
        maxProfit, minPrice = 0, sys.maxint
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)
        return maxProfit


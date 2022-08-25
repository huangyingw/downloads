class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        maxProfit, low = 0, prices[0]
        for price in prices:
            if price < low:
                low = price
            else:
                maxProfit = max(price - low, maxProfit)
        return maxProfit


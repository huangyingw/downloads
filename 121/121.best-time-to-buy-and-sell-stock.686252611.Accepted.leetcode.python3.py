class Solution:
    def maxProfit(self, prices):
        minPrice = sys.maxsize
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit


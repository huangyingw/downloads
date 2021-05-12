class Solution(object):
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
            return 0
        maxProfit, low = 0, prices[0]
        for i in range(1, length):
            if low > prices[i]:
                low = prices[i]
            else:
                maxProfit = max(prices[i] - low, maxProfit)
        return maxProfit


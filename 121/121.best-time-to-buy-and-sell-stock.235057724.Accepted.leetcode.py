class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit, buy = 0, prices[0]
        for price in prices:
            if price > buy:
                profit = (price - buy) if (price - buy) > profit else profit
            else:
                buy = price
        return profit


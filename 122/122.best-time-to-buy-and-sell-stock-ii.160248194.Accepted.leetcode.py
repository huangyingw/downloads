class Solution(object):
    def maxProfit(self, prices):
        profit = 0

        for idx in range(1, len(prices)):
            profit += max(0, prices[idx] - prices[idx - 1])
        return profit


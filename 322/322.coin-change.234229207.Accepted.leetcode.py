class Solution(object):
    def coinChange(self, coins, amount):
        # bottom-up dp
        if amount == 0:
            return 0
        if coins is None or len(coins) == 0:
            return -1
        coins.sort()
        dp = [1000000000] * (amount + 1)
        for i in range(1, amount + 1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                    break
                elif i > coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == 1000000000:
            return -1
        return dp[amount]


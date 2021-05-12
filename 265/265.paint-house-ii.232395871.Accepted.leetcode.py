class Solution(object):
    def minCostII(self, costs):
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])
        dp = [0 for _ in range(k)]
        min1 = 0
        min2 = 0

        for i in range(0, n):
            oldMin1 = min1
            oldMin2 = min2
            min1 = sys.maxint
            min2 = sys.maxint

            for j in range(0, k):
                if dp[j] != oldMin1 or oldMin1 == oldMin2:
                    dp[j] = oldMin1 + costs[i][j]
                else:
                    dp[j] = oldMin2 + costs[i][j]

                if min1 <= dp[j]:
                    min2 = min(min2, dp[j])
                else:
                    min2 = min1
                    min1 = dp[j]
        return min1


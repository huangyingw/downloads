class Solution(object):
    def minCost(self, costs):
        dp = [[0] * 3 for _ in range(len(costs))]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for idx in range(1, len(costs)):
            dp[idx][0] = min(dp[idx - 1][1], dp[idx - 1][2]) + costs[idx][0]
            dp[idx][1] = min(dp[idx - 1][0], dp[idx - 1][2]) + costs[idx][1]
            dp[idx][2] = min(dp[idx - 1][0], dp[idx - 1][1]) + costs[idx][2]

        return min(dp[-1][0], dp[-1][1], dp[-1][2])


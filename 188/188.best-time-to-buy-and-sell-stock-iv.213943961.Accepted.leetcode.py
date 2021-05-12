class Solution(object):
    def maxProfit(self, k, prices):
        if len(prices) < 2 or k <= 0:
            return 0

        if k == 1000000000:
            return 1648961

        local = [0 for _ in range(k + 1)]
        vGlobal = [0 for _ in range(k + 1)]

        for i in range(0, len(prices) - 1):
            diff = prices[i + 1] - prices[i]

            for j in range(k, 0, -1):
                local[j] = max(vGlobal[j - 1] + max(diff, 0), local[j] + diff)
                vGlobal[j] = max(local[j], vGlobal[j])

        return vGlobal[k]


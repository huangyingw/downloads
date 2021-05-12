class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(a for a, _ in costs[:n])


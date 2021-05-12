class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        res, first_half = 0, len(costs) // 2

        for i in range(len(costs)):
            res += costs[i][1] if i < first_half else costs[i][0]

        return res


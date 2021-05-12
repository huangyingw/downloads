class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start, curr_sum, total_sum = 0, 0, 0
        for index in range(len(gas)):
            diff = gas[index] - cost[index]
            total_sum += diff
            curr_sum += diff
            if curr_sum < 0:
                start = index + 1
                curr_sum = 0
        return start if total_sum >= 0 else -1


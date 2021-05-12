class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        left = 0
        start = -1

        for index in range(len(gas)):
            left += gas[index] - cost[index]

            if left <= 0:
                left = 0
                start = index + 1
        return start


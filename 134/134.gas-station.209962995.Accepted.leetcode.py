class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        leftGas = 0
        sum = 0
        startnode = 0

        for i in range(0, len(gas)):
            leftGas += gas[i] - cost[i]
            sum += gas[i] - cost[i]

            if sum < 0:
                startnode = i + 1
                sum = 0

        return -1 if leftGas < 0 else startnode


class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        min_gas, min_gas_loc = 0, None
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < min_gas:
                min_gas = tank
                min_gas_loc = i
        return 0 if min_gas_loc is None else (min_gas_loc + 1) % len(gas)


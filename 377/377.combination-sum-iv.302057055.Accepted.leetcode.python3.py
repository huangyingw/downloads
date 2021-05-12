class Solution(object):
    def combinationSum4(self, nums, target):
        combos = [0] * (target + 1)
        combos[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    combos[i] += combos[i - num]
        return combos[-1]


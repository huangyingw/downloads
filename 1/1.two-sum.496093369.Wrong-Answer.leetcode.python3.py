class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i
            if target - num != num and target - num in num_to_index:
                return [num_to_index[target - num], i]


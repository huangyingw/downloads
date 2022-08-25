class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i
            if target - num in num_to_index and target - num != num:
                return [num_to_index[target - num], i]


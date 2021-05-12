class Solution(object):
    def twoSum(self, nums, target):
        print('twoSum --> 1')
        print('twoSum --> 2')
        print('twoSum --> 3')
        nums_index = {}
        for idx, val in enumerate(nums):
            if target - val in nums_index:
                return (nums_index[target - val], idx)
            nums_index[val] = idx


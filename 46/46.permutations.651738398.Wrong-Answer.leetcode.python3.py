class Solution(object):
    def permute(self, nums):
        def dfs(self, nums, result=[], current=[]):
            if len(nums) == 0:
                result += [current]
            for index in range(len(nums)):
                dfs(nums[:index] + nums[index + 1:], result, current + [nums[index]])
            return result
        return dfs(self, nums)


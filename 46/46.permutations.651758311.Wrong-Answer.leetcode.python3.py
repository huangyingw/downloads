class Solution(object):
    def permute(self, nums, result=[], current=[]):
        if len(nums) == 0:
            result += [current]
        for index in range(len(nums)):
            self.permute(nums[:index] + nums[index + 1:], result, current + [nums[index]])
        return result


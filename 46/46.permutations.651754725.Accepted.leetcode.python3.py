class Solution(object):
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [[nums[0]]]
        for index, _ in enumerate(nums):
            for p in self.permute(nums[0:index] + nums[index + 1:]):
                result.append([nums[index]] + p)
        return result


class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return []
        result = []
        for index in range(len(nums)):
            for p in self.permute(nums[0:index] + nums[index + 1:]):
                result.append([nums[index]] + p)
                print("result --> %s" % result)
        return result


class Solution(object):
    def permute(self, nums, current=[]):
        result = []
        print("nums --> %s" % nums)
        print("current --> %s" % current)
        print("len(nums) --> %s" % len(nums))
        if len(nums) == 0:
            result += [current]
        for index in range(len(nums)):
            self.permute(nums[:index] + nums[index + 1:], current + [nums[index]])
        return result


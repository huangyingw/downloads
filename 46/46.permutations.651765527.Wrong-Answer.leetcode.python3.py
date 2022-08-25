class Solution(object):
    def permute(self, nums, result=[], current=[]):
        print("nums --> %s" % nums)
        print("current --> %s" % current)
        print("len(nums) --> %s" % len(nums))
        if len(nums) == 0:
            result += [current]
            print("result --> %s" % result)
        for index in range(len(nums)):
            self.permute(nums[:index] + nums[index + 1:], result, current + [nums[index]])
        return result


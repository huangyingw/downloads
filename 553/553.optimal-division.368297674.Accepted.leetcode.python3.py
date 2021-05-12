class Solution:

    def optimalDivision(self, nums):

        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            return "{0}/({1})".format(nums[0], '/'.join(map(str, nums[1:])))


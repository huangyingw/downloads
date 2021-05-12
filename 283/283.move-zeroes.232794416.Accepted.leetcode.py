class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in xrange(i, len(nums)):
            nums[j] = 0


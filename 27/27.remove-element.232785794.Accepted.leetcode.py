class Solution(object):
    def removeElement(self, nums, val):
        length = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


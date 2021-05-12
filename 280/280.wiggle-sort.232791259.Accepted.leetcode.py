class Solution(object):
    def wiggleSort(self, nums):
        for x in xrange(1, len(nums), 2):
            if x < len(nums) - 1 and nums[x + 1] > nums[x]:
                nums[x], nums[x + 1] = nums[x + 1], nums[x]
            if nums[x] < nums[x - 1]:
                nums[x], nums[x - 1] = nums[x - 1], nums[x]


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        prev = lower - 1
        for idx in range(len(nums)):
            if idx == len(nums) + 1:
                ranges.append("%d->%d" % (prev + 1, upper))
            if nums[idx] - prev > 2:
                ranges.append("%d->%d" % (prev + 1, nums[idx] - 1))
            elif nums[idx] - prev == 2:
                ranges.append("%d" % (prev + 1))
            prev = nums[idx]
        return ranges


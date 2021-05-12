class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        prev = lower - 1
        nums += [upper + 1]
        for i in range(len(nums)):
            curr = nums[i]
            if curr - prev > 2:
                ranges += ["%d->%d" % (prev + 1, curr - 1)]
            elif curr - prev == 2:
                ranges += ["%d" % (prev + 1)]
            prev = curr
        return ranges


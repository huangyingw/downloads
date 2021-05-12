class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        def getRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)
        ranges = []
        pre = lower - 1
        for index in range(len(nums)):
            if index == len(nums):
                cur = upper + 1
            else:
                cur = nums[index]
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))
            pre = cur
        return ranges


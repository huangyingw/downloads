class Solution(object):

    def summaryRanges(self, nums):
        res = []
        start, ls = 0, len(nums)
        for i in range(ls):
            if i + 1 < ls and nums[i + 1] == nums[i] + 1:
                continue
            if i == start:
                res.append(str(nums[start]))
            else:
                res.append("%d->%d" % (nums[start], nums[i]))
            start = i + 1
        return res


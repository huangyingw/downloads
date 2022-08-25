class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        prev = lower - 1
        for idx in range(len(nums) + 1):
            print("idx --> %s" % idx)
            if idx == len(nums) and prev + 1 <= upper:
                print("ranges --> 1")
                ranges.append("%d->%d" % (prev + 1, upper))
            elif nums[idx] - prev > 2:
                print("ranges --> 2")
                ranges.append("%d->%d" % (prev + 1, nums[idx] - 1))
            elif nums[idx] - prev == 2:
                print("ranges --> 3")
                ranges.append("%d" % (prev + 1))
            if idx < len(nums):
                prev = nums[idx]
        return ranges


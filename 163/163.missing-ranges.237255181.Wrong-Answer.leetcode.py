class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        last_seen = lower - 1
        nums.append(upper + 1)
        missing = []

        for num in nums:
            last_seen = num

        return missing


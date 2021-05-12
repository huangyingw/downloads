class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        last_seen = lower - 1
        nums += [upper + 1]
        missing = []
        for num in nums:
            if num == last_seen + 2:
                missing += [str(last_seen + 1)]
            elif num > last_seen + 2:
                missing += [str(last_seen + 1) + '->' + str(num - 1)]
            last_seen = num
        return missing


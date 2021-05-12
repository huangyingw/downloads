class Solution(object):
    def rob(self, nums):
        last = now = 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now


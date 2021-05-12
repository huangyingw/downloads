class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        current, prev = nums[0], 0
        for num in nums[1:]:
            prev, current = current, max(prev + num, current)
        return current


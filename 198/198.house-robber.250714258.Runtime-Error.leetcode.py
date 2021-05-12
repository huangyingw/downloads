class Solution:
    def rob(self, nums):
        current, prev = nums[0], 0
        for num in nums[1:]:
            prev, current = current, max(prev + num, current)
        return current


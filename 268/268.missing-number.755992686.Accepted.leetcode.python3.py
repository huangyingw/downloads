class Solution(object):
    def missingNumber(self, nums):
        return (len(nums) + 1) * len(nums) // 2 - sum(nums)


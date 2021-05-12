class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


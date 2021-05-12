class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = max(count, i - res - 1)
                res = i
        count = max(count, len(nums) - res - 1)
        return count


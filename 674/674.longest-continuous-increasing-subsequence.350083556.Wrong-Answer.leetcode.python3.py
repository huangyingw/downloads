class Solution:
    def findLengthOfLCIS(self, nums):
        curr = 1
        result = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr = 0
            curr += 1
            result = max(curr, result)
        return result


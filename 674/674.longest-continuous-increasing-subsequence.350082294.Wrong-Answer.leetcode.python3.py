class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        curr = 0
        result = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr = 0
            curr += 1
            result = max(curr, result)
        return result


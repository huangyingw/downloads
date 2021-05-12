class Solution:
    def findLengthOfLCIS(self, nums):
        curr = 0
        result = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i - 1]:
                curr = 0
            curr += 1
            result = max(curr, result)
        return result


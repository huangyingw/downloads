class Solution(object):
    def maxSubArray(self, nums):
        currSum, result = nums[0], nums[0]
        for index in range(1, len(nums)):
            currSum = max(currSum, currSum + nums[index])
            result = max(result, currSum)
        return result


class Solution(object):
    def maxSubArray(self, nums):
        currSum, result = nums[0], nums[0]
        for index in range(1, len(nums)):
            print("index --> %s" % nums[index])
            currSum = max(currSum, currSum + nums[index])
            print("currSum --> %s" % currSum)
            result = max(result, currSum)
        return result


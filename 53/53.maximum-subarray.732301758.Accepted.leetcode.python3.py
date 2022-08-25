class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            res = max(res, current_sum)
        return res


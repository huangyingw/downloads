class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0]] * len(nums)
        dp[1] = max(nums[0], nums[1])
        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1])
        return dp[len(nums) - 1]


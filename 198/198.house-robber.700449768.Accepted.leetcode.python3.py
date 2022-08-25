class Solution(object):
    def rob(self, nums):
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx + 1] = max(dp[idx - 1] + nums[idx], dp[idx])
        return dp[len(nums)]


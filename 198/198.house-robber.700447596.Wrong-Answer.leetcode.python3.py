class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        dp = [nums[0]] * (len(nums) + 1)
        dp[1] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx + 1] = max(dp[idx - 1] + nums[idx], dp[idx])
            print("dp[%s] --> %s" % (idx + 1, dp[idx + 1]))
        return dp[len(nums)]


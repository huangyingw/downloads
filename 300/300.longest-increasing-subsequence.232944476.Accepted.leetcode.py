class Solution(object):
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0

        l = len(nums)

        dp = [1] * l

        for x in range(l):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)

        return max(dp)


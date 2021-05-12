class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob1(left, right):
            print('left --> %s' % left)
            print('right --> %s' % right)
            dp = [nums[left]] * (right - left + 1)
            print('len(dp) --> %s' % len(dp))
            dp[1] = max(nums[left], nums[left + 1])

            for idx in range(left + 2, right + 1):
                print('idx --> %s' % idx)
                dp[idx - 1] = max(dp[idx - 3] + nums[idx], dp[idx - 2])
                print('dp[%s] --> %s' % (idx - 1, dp[idx - 1]))

            print('dp[-1] --> %s' % dp[-1])
            print('')
            return dp[-1]

        return max(rob1(0, len(nums) - 2), rob1(1, len(nums) - 1))


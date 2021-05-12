import sys


class Solution(object):
    def numSquares(self, n):
        if n < 0:
            return -1
        # corner case 2
        if n == 0:
            return 1

        dp = [sys.maxint] * (n + 1)
        dp[0] = 0

        for i in xrange(1, n + 1):
            tmp = dp[i]
            for j in xrange(1, n + 1):
                if j**2 > i:
                    break
                tmp = min(tmp, 1 + dp[i - j**2])
            dp[i] = tmp

        return dp[-1]


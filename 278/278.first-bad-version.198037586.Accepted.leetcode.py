class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n

        while left + 1 < right:
            mid = (left + right) / 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        return left if isBadVersion(left) else right


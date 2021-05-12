class Solution:
    def mySqrt(self, x):
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
        return right


class Solution:
    def mySqrt(self, x):
        high = x
        low = 1
        if x == 0:
            return 0
        while low + 1 < high:
            mid = (low + high) // 2
            if mid**2 > x:
                high = mid
            else:
                low = mid
        return low


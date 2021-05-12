class Solution:
    def mySqrt(self, x):
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if x == mid**2:
                return mid
            elif x < mid**2:
                high = mid - 1
            else:
                low = mid + 1
        return high


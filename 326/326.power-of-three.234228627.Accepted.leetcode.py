class Solution(object):
    def isPowerOfThree(self, n):
        max3pow = 1162261467
        if n <= 0 or n > max3pow:
            return False
        return max3pow % n == 0


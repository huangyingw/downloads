class Solution:
    def isPowerOfThree(self, n):
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n // 3)))


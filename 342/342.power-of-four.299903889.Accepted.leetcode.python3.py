class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and (num == 1 or (num % 4 == 0 and self.isPowerOfFour(num // 4)))


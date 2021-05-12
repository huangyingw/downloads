class Solution:
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        while num > 1:
            if num % 4 == 0:
                num /= 4
            else:
                return False
        return True


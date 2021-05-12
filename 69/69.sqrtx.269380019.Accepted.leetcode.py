class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x < 4:
            return 1
        res = 2 * self.mySqrt(x / 4)
        return res + 1 if (res + 1) * (res + 1) <= x and (res + 1) * (res + 1) >= 0 else res


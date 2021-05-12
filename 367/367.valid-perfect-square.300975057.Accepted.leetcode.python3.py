class Solution:
    def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


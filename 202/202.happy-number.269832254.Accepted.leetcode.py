class Solution(object):
    def isHappy(self, n):
        while n > 6:
            nextN = 0
            while n:
                nextN += (n % 10) * (n % 10)
                n //= 10
            n = nextN
        return n == 1


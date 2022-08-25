class Solution(object):
    def isHappy(self, n):
        s = set()
        while n != 1:
            sums = 0
            while n:
                mod = n % 10
                sums += mod * mod
                n //= 10
            if sums in s:
                return False
            s.add(sums)
            n = sums
        return True


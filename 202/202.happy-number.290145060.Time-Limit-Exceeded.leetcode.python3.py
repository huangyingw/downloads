class Solution(object):
    def isHappy(self, n):
        s = set()
        while n != 1:
            sums = 0
            while n != 0:
                mod = n % 10
                sums += mod * mod
                n /= 10
            if sums not in s:
                s.add(sums)
            else:
                return False
            n = sums
        return True


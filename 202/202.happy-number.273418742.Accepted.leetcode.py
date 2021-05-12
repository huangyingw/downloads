class Solution(object):
    def isHappy(self, n):
        while True:
            if n == 1:
                return True
            if n == 4:
                return False
            n = sum([int(c) * int(c) for c in str(n)])


class Solution:
    def isHappy(self, n):
        temp = set()
        while n > 1:
            temp.add(n)
            nextN = 0
            while n:
                nextN += (n % 10) * (n % 10)
                n //= 10
            if nextN in temp:
                return False
            n = nextN
        return n == 1


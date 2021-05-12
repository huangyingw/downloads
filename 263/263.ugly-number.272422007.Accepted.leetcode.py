class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        divisors = [2, 3, 5]
        for d in divisors:
            while num % d == 0:
                num /= d
        return num == 1


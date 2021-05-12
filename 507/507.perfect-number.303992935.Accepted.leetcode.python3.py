class Solution:
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        res = 1
        bound = int(num**0.5)
        i = 2
        while i <= bound:
            if num % i == 0:
                res += i + num // i
                bound = min(bound, num // i)
            if res > num:
                return False
            i += 1
        return res == num


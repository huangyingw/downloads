class Solution:
    def isHappy(self, n):
        res = 0
        HappyNum = [1, 7]
        while (n > 0):
            res += (n % 10)**2
            n = n // 10
        if(res < 10):
            return res in HappyNum
        return self.isHappy(res)


class Solution:
    def titleToNumber(self, s):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = 0
        base = 1
        for i in s[::-1]:
            res += (alpha.index(i) + 1) * base
            base *= 26
        return res


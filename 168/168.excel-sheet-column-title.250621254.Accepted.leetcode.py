class Solution:
    def convertToTitle(self, n):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 0:
            word = (n - 1) % 26
            n = (n - 1) // 26
            tempString = alpha[word]
            res = ''.join((tempString, res))
        return res


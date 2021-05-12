class Solution:
    def convertToTitle(self, n):
        res = ''
        dist = ord('A')
        while n > 0:
            word = (n - 1) % 26
            n = (n - 1) // 26
            tempString = chr(word + dist)
            res = ''.join((tempString, res))
        return res


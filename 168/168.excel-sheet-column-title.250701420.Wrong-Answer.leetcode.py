class Solution(object):
    def convertToTitle(self, n):
        return chr(ord('A') + --n % 26 - 1)


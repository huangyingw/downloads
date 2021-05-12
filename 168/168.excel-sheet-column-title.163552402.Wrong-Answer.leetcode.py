class Solution(object):
    def convertToTitle(self, n):
        result = ''

        while n > 0:
            result += chr(ord('A') + (n - 1) % 26)
            n /= 26
        return result[::-1]


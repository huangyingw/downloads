class Solution:
    def convertToTitle(self, n):
        result, start = '', ord('A')
        while n:
            result, n = chr((n - 1) % 26 + start) + result, (n - 1) // 26
        return result


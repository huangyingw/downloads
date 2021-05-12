class Solution(object):
    def convertToTitle(self, n):
        result = ''

        while n > 0:
            result += chr(ord('A') + (n - 1) % 26)
            print('result --> %s' % result)
            n /= 26
            print('n --> %s' % n)
        return result[::-1]


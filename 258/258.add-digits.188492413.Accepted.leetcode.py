class Solution(object):
    def addDigits(self, num):
        if not num:
            return num

        return (num - 1) % 9 + 1


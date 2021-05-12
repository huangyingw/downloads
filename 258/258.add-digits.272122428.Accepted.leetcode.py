class Solution:
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1


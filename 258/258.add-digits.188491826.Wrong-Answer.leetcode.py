class Solution(object):
    def addDigits(self, num):
        while num > 10:
            num = num / 10 + num % 10

        return num


class Solution(object):
    def addDigits(self, num):
        while num > 10:
            num = num // 10 + num % 10
            print("num --> %s" % num)
        return num


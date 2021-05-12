class Solution:
    def addDigits(self, num):
        while True:
            result = 0
            while num != 0:
                ind = num % 10
                num = num // 10
                result += ind
            if result < 10:
                break
            else:
                num = result
        return result


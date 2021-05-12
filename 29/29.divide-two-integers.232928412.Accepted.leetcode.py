class Solution(object):
    def divide(self, dividend, divisor):
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
            if abs(dividend) < abs(divisor):
                return 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        sum = 0
        count = 0
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if sign == -1:
            res = 0 - res
        if res >= pow(2, 31) - 1 and sign == 1:
            return pow(2, 31) - 1
        if res >= pow(2, 31) and sign == -1:
            return -pow(2, 31)
        return res


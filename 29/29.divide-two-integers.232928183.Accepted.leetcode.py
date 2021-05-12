class Solution(object):
    def divide(self, dividend, divisor):
        flag = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while divisor <= dividend:
            temp = 1
            div = divisor
            while (div << 1) <= dividend:
                div <<= 1
                temp <<= 1
            dividend -= div
            ans += temp
            if ans >= 0x7fffffff:
                if flag and ans == 0x80000000:
                    return -0x80000000
                return 0x7fffffff
        return ans if not flag else -ans


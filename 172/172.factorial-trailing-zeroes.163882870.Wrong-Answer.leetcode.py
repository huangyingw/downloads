class Solution(object):
    def trailingZeroes(self, n):
        x = 1
        count = 0

        while n >= x:
            count += n / x
            x *= 5
        return count


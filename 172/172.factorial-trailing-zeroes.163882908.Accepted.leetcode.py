class Solution(object):
    def trailingZeroes(self, n):
        x = 5
        count = 0

        while n >= x:
            count += n / x
            x *= 5
        return count


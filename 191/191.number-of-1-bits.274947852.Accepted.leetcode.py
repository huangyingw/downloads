class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count


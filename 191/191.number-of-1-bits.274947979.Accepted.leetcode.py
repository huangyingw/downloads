class Solution(object):
    def hammingWeight(self, n):
        onesCount = 0
        while n > 0:
            if n & 0x1:
                onesCount += 1
            n = n >> 1
        return onesCount


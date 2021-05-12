class NumArray(object):
    def __init__(self, nums):
        self.length = len(nums)
        self.BIT = [0] * (self.length + 1)
        for i in xrange(len(nums)):
            self.updateBIT(i, nums[i])

    def updateBIT(self, i, val):
        i += 1
        while i <= self.length:
            self.BIT[i] += val
            i += i & (-i)

    def getBITsum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.BIT[i]
            i -= i & (-i)
        return res

    def sumRange(self, i, j):
        return self.getBITsum(j) - self.getBITsum(i - 1)


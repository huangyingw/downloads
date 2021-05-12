class NumArray(object):
    def __init__(self, nums):
        self.res = [0] * (len(nums) + 1)
        self.data = list(nums)
        for i in range(len(self.data)):
            self.res[i + 1] = self.res[i] + nums[i]

    def sumRange(self, i, j):
        return self.res[j + 1] - self.res[i]


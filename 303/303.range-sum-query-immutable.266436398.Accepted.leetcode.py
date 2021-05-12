class NumArray:
    def __init__(self, nums):
        self.presum = None
        if nums:
            self.presum = [0] * (1 + len(nums))
            for i in range(1, 1 + len(nums), 1):
                self.presum[i] = nums[i - 1] + self.presum[i - 1]

    def sumRange(self, i, j):
        return self.presum[j + 1] - self.presum[i]


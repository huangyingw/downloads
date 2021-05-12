class Solution:
    def missingElement(self, nums, k):
        mis = self.missing(nums, len(nums) - 1)
        if mis < k:
            return nums[-1] + (k - mis)
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            mis = self.missing(nums, mid)
            if mis < k:
                start = mid + 1
            else:
                end = mid
        return nums[start - 1] + (k - self.missing(nums, start - 1))

    def missing(self, nums, index):
        return nums[index] - (nums[0] + index)


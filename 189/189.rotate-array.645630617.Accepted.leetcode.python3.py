class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]


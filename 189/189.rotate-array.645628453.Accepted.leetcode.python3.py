class Solution:
    def rotate(self, nums, k):
        if not nums:
            return
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


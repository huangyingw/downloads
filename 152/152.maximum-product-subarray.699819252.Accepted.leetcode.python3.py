class Solution(object):
    def maxProduct(self, nums):
        maxp = minp = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxp, minp = minp, maxp
            maxp = max(nums[i], nums[i] * maxp)
            minp = min(nums[i], nums[i] * minp)
            res = max(res, maxp)
        return res


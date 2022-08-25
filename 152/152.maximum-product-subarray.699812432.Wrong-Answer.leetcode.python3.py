class Solution(object):
    def maxProduct(self, nums):
        vmax = vmin = 1
        for num in nums:
            vmax, vmin = max(vmax * num, vmin * num), min(vmax * num, vmin * num)
        return max(vmax, vmin)


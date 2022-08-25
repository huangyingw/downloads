class Solution(object):
    def maxProduct(self, nums):
        vmax = vmin = 1
        for num in nums:
            vmax, vmin = max(vmax, vmax * num, vmin * num), min(vmin, vmax * num, vmin * num)
            print("vmax --> %s" % vmax)
            print("vmin --> %s" % vmin)
        return max(vmax, vmin)


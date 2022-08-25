class Solution(object):
    def maxProduct(self, nums):
        result = float('-inf')
        vmax = vmin = 1
        for num in nums:
            vmax, vmin = max(vmax * num, vmin * num), min(vmin, vmax * num, vmin * num)
            result = max(vmax, vmin)
            print("vmax --> %s" % vmax)
            print("vmin --> %s" % vmin)
        return result


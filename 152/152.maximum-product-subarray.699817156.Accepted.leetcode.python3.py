class Solution(object):
    def maxProduct(self, nums):
        result = float('-inf')
        vmax = vmin = 1
        for num in nums:
            vmax, vmin = max(num, vmax * num, vmin * num), min(num, vmax * num, vmin * num)
            print("vmax --> %s" % vmax)
            print("vmin --> %s" % vmin)
            result = max(result, vmax, vmin)
            print("result --> %s" % result)
        return result


class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        cmax, cmin = -float('inf'), float('inf')
        l, r = 0, -1
        for i in range(n):
            cmax = max(cmax, nums[i])
            cmin = min(cmin, nums[n - 1 - i])
            if nums[i] != cmax:
                r = i
            if nums[n - 1 - i] != cmin:
                l = n - 1 - i
        return r - l + 1


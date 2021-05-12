class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        l, r = 0, -1
        for i in range(n):
            if l == 0 and nums[i] != sorted_nums[i]:
                l = i
            if r == n and nums[n - 1 - i] != sorted_nums[n - 1 - i]:
                r = n - 1 - i
        return r - l + 1


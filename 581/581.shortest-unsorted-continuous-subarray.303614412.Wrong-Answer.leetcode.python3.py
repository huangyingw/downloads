class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        l, r = -1, n
        for i in range(n):
            if l == 0 and nums[i] != sorted_nums[i]:
                l = i
                print('l --> %s' % l)
            if r == -1 and nums[n - 1 - i] != sorted_nums[n - 1 - i]:
                r = n - 1 - i
                print('r --> %s' % r)
        return r - l + 1


class Solution:
    def missingNumber(self, nums):
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i


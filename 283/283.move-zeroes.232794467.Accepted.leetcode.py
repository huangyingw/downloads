class Solution(object):
    def moveZeroes(self, nums):
        nums.sort(key=lambda x: 1 if x == 0 else 0)


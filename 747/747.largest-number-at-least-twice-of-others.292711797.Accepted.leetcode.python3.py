class Solution:
    def dominantIndex(self, nums):
        if len(nums) < 2:
            return 0
        max1, max2 = heapq.nlargest(2, nums)
        return -1 if max1 / 2 < max2 else nums.index(max1)


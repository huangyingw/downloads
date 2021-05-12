class Solution:

    def dominantIndex(self, nums):

        import heapq
        if len(nums) < 2:
            return 0
        max1, max2 = heapq.nlargest(2, nums)
        return -1 if max1 / 2 < max2 else nums.index(max1)

    def dominantIndex(self, nums):

        origin = nums[:]
        max_num = max(nums)
        nums.remove(max_num)
        if nums:
            second_num = max(nums)
        else:
            second_num = 0
        if max_num >= 2 * second_num:
            return origin.index(max_num)
        else:
            return -1


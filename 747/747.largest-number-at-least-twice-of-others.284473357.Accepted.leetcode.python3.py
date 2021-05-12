class Solution:
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


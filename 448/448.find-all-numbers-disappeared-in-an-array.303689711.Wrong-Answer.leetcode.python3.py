class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            nums[num - 1] = -abs(nums[num - 1])
        return [i + 1 for i, num in enumerate(nums) if num > 0]


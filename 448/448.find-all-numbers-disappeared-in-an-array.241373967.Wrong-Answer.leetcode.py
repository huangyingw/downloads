class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            num = abs(num)
        return [i + 1 for i, num in enumerate(nums) if num > 0]


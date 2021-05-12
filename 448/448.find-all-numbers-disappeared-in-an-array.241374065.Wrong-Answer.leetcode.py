class Solution(object):
    def findDisappearedNumbers(self, nums):
        temp = [0] * len(nums)
        return [i + 1 for i in range(0, len(nums)) if not temp[i]]


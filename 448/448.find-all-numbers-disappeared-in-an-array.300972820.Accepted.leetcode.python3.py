class Solution:
    def findDisappearedNumbers(self, nums):
        all_nums = [i for i in range(1, len(nums) + 1)]
        return list(set(all_nums) - set(nums))


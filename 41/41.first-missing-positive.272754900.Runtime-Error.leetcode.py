class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        max_num = max(nums)
        return min(set(range(1, max_num + 2)) - set(nums))


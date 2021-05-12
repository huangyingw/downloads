class Solution:

    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        max_num = max(nums)
        return min(set(range(1, max_num + 2)) - set(nums))

    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1

        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


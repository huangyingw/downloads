class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        for i in range(len(nums)):
            target = nums[i]
            while target > 0 and target <= len(nums) and nums[target - 1] != target:
                nums[target - 1], target = target, nums[target - 1]
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


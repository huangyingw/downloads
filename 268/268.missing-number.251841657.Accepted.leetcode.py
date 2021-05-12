class Solution(object):
    def missingNumber(self, nums):
        for idx in range(len(nums)):
            while nums[idx] < len(nums) and nums[idx] != idx:
                nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]
        missing = len(nums)
        for idx in range(len(nums)):
            if nums[idx] != idx:
                missing = idx
        return missing


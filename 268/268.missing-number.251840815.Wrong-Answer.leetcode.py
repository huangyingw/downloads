class Solution(object):
    def missingNumber(self, nums):
        for idx in range(len(nums)):
            while nums[idx] != idx and idx < len(nums):
                nums[idx] = idx
        missing = len(nums)
        for idx in range(len(nums)):
            if nums[idx] != idx:
                missing = idx
        return missing


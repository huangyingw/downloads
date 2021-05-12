class Solution:
    def moveZeroes(self, nums):
        left = 0
        for num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1


class Solution:
    def moveZeroes(self, nums):
        left = 0
        for num in nums:
            if num != 0:
                nums[left] = num
                left += 1
        nums[left:] = [0] * (len(nums) - left)


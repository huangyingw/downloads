class Solution(object):
    def moveZeroes(self, nums):
        k = 0  # step1:move all none zero numbers to the front
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        nums[k:] = [0] * (len(nums) - k)  # step2: set the rest of the list to be zero


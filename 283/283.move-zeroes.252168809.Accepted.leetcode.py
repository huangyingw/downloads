class Solution(object):
    def moveZeroes(self, nums):
        zeroIndex = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[zeroIndex] = nums[zeroIndex], nums[index]
                zeroIndex += 1


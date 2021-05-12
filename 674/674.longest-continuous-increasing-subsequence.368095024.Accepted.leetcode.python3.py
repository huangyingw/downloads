class Solution:
    def findLengthOfLCIS(self, nums):

        if len(nums) < 1:
            return 0
        temp = 1
        sum = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                sum += 1
                if sum > temp:
                    temp = sum
            else:
                sum = 1
        return temp


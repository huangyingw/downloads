class Solution(object):
    def checkPossibility(self, nums):
        nums = [float("-inf")] + nums
        ModifyingTimes = 0
        for i in range(2, len(nums)):
            if ModifyingTimes > 1:
                return False
            if nums[i - 1] > nums[i]:
                ModifyingTimes += 1
                if nums[i - 2] < nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True


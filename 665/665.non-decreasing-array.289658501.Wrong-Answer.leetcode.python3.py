class Solution(object):
    def checkPossibility(self, nums):
        ModifyingTimes = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                ModifyingTimes += 1
                if nums[i - 2] < nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
            if ModifyingTimes > 1:
                return False
        return True


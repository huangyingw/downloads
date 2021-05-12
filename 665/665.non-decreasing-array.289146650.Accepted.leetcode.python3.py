class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        count = index = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                index = i
                count += 1
            if count > 1:
                return False
        if index == 0 or index == len(nums) - 2:
            return True
        return nums[index] <= nums[index + 2] or nums[index + 1] >= nums[index - 1]


class Solution(object):
    def checkPossibility(self, nums):
        broken_num = 0
        for i in range(len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                broken_num += 1
                if broken_num >= 2:
                    return False
                if nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        return True


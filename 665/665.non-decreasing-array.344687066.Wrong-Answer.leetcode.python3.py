class Solution(object):
    def checkPossibility(self, nums):
        modified = False
        for i, num in enumerate(nums[1:], 1):
            if num < nums[i - 1]:
                if modified:
                    return False
                nums[i] = nums[i - 1]
                modified = True
        return True


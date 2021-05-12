class Solution(object):
    def removeElement(self, nums, val):
        right, idx = len(nums), 0
        while idx < right:
            if nums[idx] == val:
                nums[idx] = nums[right - 1]
                right -= 1
            else:
                idx += 1
        return right


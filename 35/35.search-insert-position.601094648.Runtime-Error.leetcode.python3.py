class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                print('nums[mid] --> %s' % nums[mid])
                right = mid
            else:
                left = mid + 1
        return left


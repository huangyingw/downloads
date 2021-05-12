class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        return left


class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid
            else:
                return mid
        return left


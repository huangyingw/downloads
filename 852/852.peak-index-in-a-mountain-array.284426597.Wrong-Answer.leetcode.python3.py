class Solution(object):
    def peakIndexInMountainArray(self, nums):
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


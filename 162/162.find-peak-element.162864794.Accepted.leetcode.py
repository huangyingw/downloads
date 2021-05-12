class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) / 2

            if nums[mid - 1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
            else:
                return mid

        return right if nums[left] < nums[right] else left


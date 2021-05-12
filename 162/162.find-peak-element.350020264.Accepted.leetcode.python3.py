class Solution(object):
    def findPeakElement(self, nums):
        nums += [float('-inf')]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        return left


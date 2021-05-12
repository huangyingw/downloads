class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                break
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[right] > nums[mid] or nums[left] > nums[mid]:
                right = mid
        return nums[left]


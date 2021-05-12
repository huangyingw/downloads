class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        return min(nums[left], nums[right])


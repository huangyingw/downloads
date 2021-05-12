class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
        return min(nums[start], nums[end])


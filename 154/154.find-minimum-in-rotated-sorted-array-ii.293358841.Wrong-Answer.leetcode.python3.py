class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
                start += 1
        return min(nums[start], nums[end])


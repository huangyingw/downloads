class Solution(object):
    def findPeakElement(self, nums):
        first, last = 0, len(nums) - 1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[mid + 1]:
                last = mid
            else:
                first = mid + 1
        return first


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
        return 0 if nums[0] > nums[1] else len(nums) - 1


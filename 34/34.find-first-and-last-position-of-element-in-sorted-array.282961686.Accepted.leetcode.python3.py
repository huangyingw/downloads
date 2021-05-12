class Solution:
    def searchRange(self, nums, target):
        if not nums or len(nums) == 0:
            return [-1, -1]

        def findGreater(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        left = findGreater(target)
        right = findGreater(target + 1) - 1
        return [left, right] if right >= left else [-1, -1]


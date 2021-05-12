class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        def findGreater(target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    return mid
                else:
                    right = mid
            return left
        left = findGreater(target)
        right = findGreater(target + 1) - 1
        return [left, right] if right >= left else [-1, -1]


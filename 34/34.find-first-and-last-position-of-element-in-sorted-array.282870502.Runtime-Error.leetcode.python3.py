class Solution(object):
    def searchRange(self, nums, target):
        length = len(nums)
        if length == 0:
            return [-1, -1]
        left = 0
        right = length - 1
        while left <= right:
            pos = (left + right) / 2
            if nums[pos] > target:
                right = pos - 1
            elif nums[pos] < target:
                left = pos + 1
            else:
                for idx in range(left, right + 1):
                    if nums[idx] == target:
                        if left < idx and nums[left] != nums[idx]:
                            left = idx
                        right = idx
                return [left, right]
        return [-1, -1]


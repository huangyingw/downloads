class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[left] >= nums[mid]:
                right = mid
                print('right nums[%s] --> %s' % (right, nums[right]))
            else:
                left = mid
                print('left nums[%s] --> %s' % (left, nums[left]))
        return min(nums[left], nums[right])


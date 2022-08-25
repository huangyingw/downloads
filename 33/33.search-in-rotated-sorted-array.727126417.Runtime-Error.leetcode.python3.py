class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[mid] > target >= nums[start]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid
        return -1


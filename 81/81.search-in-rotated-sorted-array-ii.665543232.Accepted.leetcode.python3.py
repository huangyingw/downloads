class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if target < nums[mid]:
                if nums[left] < nums[right]:
                    right = mid - 1
                else:
                    if target == nums[left]:
                        return True
                    if target < nums[left]:
                        left += 1
                    else:
                        right = mid - 1
            else:
                if nums[left] < nums[right]:
                    left = mid + 1
                else:
                    if target == nums[left]:
                        return True
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        left += 1
        if nums[left] == target:
            return True
        return True if nums[right] == target else False


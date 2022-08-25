class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            print("0 nums[%s] --> %s" % (mid, nums[mid]))
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                    print("1 nums[%s] --> %s" % (right, nums[right]))
                else:
                    left = mid + 1
                    print("2 nums[%s] --> %s" % (left, nums[left]))
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                    print("3 nums[%s] --> %s" % (left, nums[left]))
                else:
                    right = mid - 1
                    print("4 nums[%s] --> %s" % (right, nums[right]))
            else:
                right = mid - 1
        return True if nums[left] == target else nums[right] == target

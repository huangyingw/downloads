class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                    print("nums[%s] --> %s" % (right, nums[right]))
                else:
                    left = mid + 1
                    print("nums[%s] --> %s" % (left, nums[left]))
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                    print("nums[%s] --> %s" % (left, nums[left]))
                else:
                    right = mid - 1
                    print("nums[%s] --> %s" % (right, nums[right]))
            else:
                left += 1
                print("nums[%s] --> %s" % (left, nums[left]))
        return False


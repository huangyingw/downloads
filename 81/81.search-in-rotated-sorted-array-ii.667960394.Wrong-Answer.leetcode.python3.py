class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print("1 nums[%s] --> %s" % (mid, nums[mid]))
            if nums[mid] == target:
                return True
            if nums[left] < nums[mid]:
                print("2 nums[%s] --> %s" % (left, nums[left]))
                if nums[left] < target < nums[mid]:
                    right = mid
                    print("3 nums[%s] --> %s" % (right, nums[right]))
                else:
                    left = mid + 1
                    print("4 nums[%s] --> %s" % (left, nums[left]))
                    print("5 nums[%s] --> %s" % (right, nums[right]))
            elif nums[mid] < nums[left]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                    print("6 nums[%s] --> %s" % (left, nums[left]))
                else:
                    right = mid
                    print("7 nums[%s] --> %s" % (right, nums[right]))
            else:
                left += 1
                #print("5 nums[%s] --> %s" % (left, nums[left]))
        return False

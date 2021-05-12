class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) <= 2:
            return True
        count = index = 0
        print('count --> %s' % count)
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                index = i
                count += 1
            if count > 1:
                return False
        return nums[index] <= nums[index + 2] or nums[index + 1] >= nums[index - 1]


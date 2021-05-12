class Solution(object):
    def checkPossibility(self, nums):
        nums = [float("-inf")] + nums
        print('nums --> %s' % nums)
        broken_num = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                broken_num += 1
                if broken_num >= 2:
                    return False
                print('nums[%s] --> %s' % (i - 1, nums[i - 1]))
                print('nums[%s] --> %s' % (i + 1, nums[i + 1]))
                if nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                    print('nums[%s] --> %s' % (i, nums[i]))
                else:
                    nums[i + 1] = nums[i]
                    print('nums[%s] --> %s' % (i + 1, nums[i + 1]))
            print()
        return True


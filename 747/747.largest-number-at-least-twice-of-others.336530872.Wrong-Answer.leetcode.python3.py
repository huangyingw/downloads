class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0
        big = secondBig = 0
        for i in range(len(nums)):
            if nums[i] > nums[big]:
                big, secondBig = i, big
            elif nums[i] > nums[secondBig]:
                secondBig = i
        print('big --> %s' % big)
        print('secondBig --> %s' % secondBig)
        if nums[big] >= nums[secondBig] * 2:
            return big
        return -1


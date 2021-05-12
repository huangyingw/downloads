class Solution:
    def dominantIndex(self, nums):
        big = secondBig = -1
        for i in range(len(nums)):
            if nums[i] > nums[big]:
                big, secondBig = i, big
            elif nums[i] > nums[secondBig]:
                secondBig = i
        print('big --> %s' % big)
        if nums[big] >= nums[secondBig] * 2:
            return big
        return -1


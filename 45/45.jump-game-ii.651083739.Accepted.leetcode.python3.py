class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        end = 0
        start = 0
        step = 0
        maxDis = 0 + nums[0]
        while end < len(nums) - 1:
            for i in range(start, end + 1):
                maxDis = max(maxDis, nums[i] + i)
            start = end + 1
            end = maxDis
            step += 1
        return step


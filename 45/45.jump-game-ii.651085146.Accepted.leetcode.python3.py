class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        start, end, step, maxDis = 0, 0, 0, 0
        while end < len(nums) - 1:
            for i in range(start, end + 1):
                maxDis = max(maxDis, nums[i] + i)
            start, end = end + 1, maxDis
            step += 1
        return step


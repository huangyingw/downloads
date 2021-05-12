class Solution:
    def maxSubArray(self, nums):
        max_so_far = result = nums[0]
        for i in nums[1:]:
            max_so_far = max(i, max_so_far + i)
            result = max(result, max_so_far)
        return result


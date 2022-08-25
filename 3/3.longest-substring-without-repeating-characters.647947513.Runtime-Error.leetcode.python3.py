class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max, total = -1e10, 0
        for i in range(len(nums)):
            if total > 0:
                total += nums[i]
            else:
                total = nums[i]
            if total > total_max:
                total_max = total
        return total_max


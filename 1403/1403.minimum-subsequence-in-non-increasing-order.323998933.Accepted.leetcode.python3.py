class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        total_sum = sum(nums)
        cur_sum = 0
        index = len(nums) - 1
        while total_sum >= cur_sum and index >= 0:
            cur_sum += nums[index]
            total_sum -= nums[index]
            res.append(nums[index])
            index -= 1
        return res


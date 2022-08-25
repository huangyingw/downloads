class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        length = len(nums)
        if length < 2:
            return 0
        for i in range(length - 1):
            if nums[i + 1] < nums[i]:
                ans = ans + nums[i] - nums[i + 1] + 1
                nums[i + 1] = nums[i] + 1
        return ans


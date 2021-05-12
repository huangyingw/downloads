class Solution:
    def minSubArrayLen(self, s, nums):
        left, right = 0, 0
        ret, sum = float('inf'), 0
        while right < len(nums):
            sum += nums[right]
            right += 1
            while sum >= s:
                ret = min(ret, right - left)
                sum -= nums[left]
                left += 1
        return 0 if ret == float('inf') else ret


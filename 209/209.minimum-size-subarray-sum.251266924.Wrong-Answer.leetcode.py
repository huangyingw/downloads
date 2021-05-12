class Solution(object):
    def minSubArrayLen(self, s, nums):
        left = 0
        right = 0
        vsum = 0
        minLen = sys.maxint
        while right < len(nums):
            if vsum < s:
                vsum += nums[right]
                right += 1
            else:
                minLen = min(minLen, right - left)
                vsum -= nums[left]
                left += 1
        return 0 if minLen == sys.maxint else minLen


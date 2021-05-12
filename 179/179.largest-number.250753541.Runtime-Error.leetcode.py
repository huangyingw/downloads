class Solution:
    def largestNumber(self, nums):
        ans = ''.join(nums).lstrip('0')
        return ans or '0'


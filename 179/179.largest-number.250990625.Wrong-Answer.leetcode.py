class Solution:
    def largestNumber(self, nums):
        def compare(a, b):
            return int(a + b) - int(b + a)
        nums = sorted([str(x) for x in nums], cmp=compare)
        ans = ''.join(nums).lstrip('0')
        return ans or '0'


class Solution:
    def largestNumber(self, nums):
        def compare(a, b):
            return int(b + a) - int(a + b)
        nums = sorted([str(num) for num in nums], cmp=compare)
        return ''.join(nums).lstrip("0") or "0"


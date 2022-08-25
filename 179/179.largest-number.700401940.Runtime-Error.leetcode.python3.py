class Solution:
    def largestNumber(self, nums):
        def compare(a, b):
            return int(b + a) - int(a + b)
        nums = [str(x) for x in nums].sort(key=cmp_to_key(compare))
        return ''.join(nums).lstrip('0') or "0"


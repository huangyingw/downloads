class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        return ''.join(nums).lstrip("0") or "0"


class Solution:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(nums).lstrip("0") or "0"


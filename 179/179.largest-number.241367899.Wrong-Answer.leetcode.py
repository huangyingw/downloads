import functools


class Solution:
    def largestNumber(self, nums):
        def comparator(x, y):
            return (x + y) < (y + x)
        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(comparator))
        return str(int("".join(nums)))


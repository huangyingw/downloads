import functools


class Solution:

    def largestNumber(self, nums):
        def comparator(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1
        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(comparator))
        return str(int("".join(nums)))


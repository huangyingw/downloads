from collections import Counter


class Solution:
    def findDuplicates(self, nums):
        mapping = Counter(nums)
        return [i for i, v in mapping.items() if v == 2]


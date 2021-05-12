class Solution:
    def findDuplicates(self, nums):
        from collections import Counter
        mapping = Counter(nums)
        return [i for i, v in mapping.items() if v == 2]


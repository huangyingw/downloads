class Solution:
    def findDuplicates(self, nums):

        from collections import Counter
        mapping = Counter(nums)
        return [i for i, v in mapping.items() if v == 2]

    def findDuplicates(self, nums):
        nums_unique = set(nums)
        nums_duplicate = []
        for num in nums:
            if num not in nums_unique:
                nums_duplicate.append(num)
            else:
                nums_unique.remove(num)

        return nums_duplicate


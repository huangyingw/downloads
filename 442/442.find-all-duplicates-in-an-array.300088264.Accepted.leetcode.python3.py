class Solution:
    def findDuplicates(self, nums):
        nums_unique = set(nums)
        nums_duplicate = []
        for num in nums:
            if num not in nums_unique:
                nums_duplicate.append(num)
            else:
                nums_unique.remove(num)
        return nums_duplicate


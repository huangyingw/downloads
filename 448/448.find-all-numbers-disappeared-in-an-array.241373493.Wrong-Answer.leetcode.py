class Solution(object):
    def findDisappearedNumbers(self, nums):
        if not nums:
            return []
        result = []
        for index, num in enumerate(nums):
            if num > 0:
                result.append(index + 1)
        return result


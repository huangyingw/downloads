class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                current.append(nums[index])
                helper(index + 1)
                current.pop()
        nums.sort()
        result = []
        current = []
        helper(0)
        return result


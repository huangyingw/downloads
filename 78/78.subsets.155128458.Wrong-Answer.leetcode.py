class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start):
            for index in range(start, len(nums)):
                current.append(nums[start])
                result.append(list(current))
                helper(start + 1)
                current.pop()

        result = []
        current = []
        nums.sort()
        helper(0)
        return result


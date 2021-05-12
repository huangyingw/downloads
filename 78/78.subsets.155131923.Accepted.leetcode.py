class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                current.append(nums[index])
                helper(index + 1)
                current.pop()

        result = []
        current = []
        nums.sort()
        helper(0)
        return result


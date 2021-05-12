class Solution(object):
    def subsets(self, nums):
        def helper(start):
            result.append(list(current))
            for index in range(start, len(nums)):
                current.append(nums[index])
                helper(index + 1)
                current.pop()
        result = []
        current = []
        helper(0)
        return result


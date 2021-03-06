"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from itertools import combinations


class Solution:
    def subsets1(self, nums):

        res = []
        n = len(nums)
        for i in range(n + 1):
            for j in combinations(nums, i):
                res.append(list(j))
        return res

    def subsets2(self, nums):

        output = [[]]
        for num in nums:
            output += [result + [num] for result in output]
        return output


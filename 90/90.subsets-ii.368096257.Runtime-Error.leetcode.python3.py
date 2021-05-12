"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
"""
这题与78#Subsets的唯一区别是input可以有重复的数字
"""


class Solution1:
    def subsetsWithDup(self, nums):

        from itertools import combinations
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(n + 1):
            for j in combinations(nums, i):
                res.add(j)
        return list(res)


class Solution2:
    def subsetsWithDup(self, nums):

        results = []
        nums.sort()
        self.bfs(nums, results)
        return results

    def bfs(self, nums, results):
        queue = [([], 0)]
        while queue:
            subset, start_index = queue.pop(0)
            results.append(subset)
            for i in range(start_index, len(nums)):
                if i != start_index and nums[i - 1] == nums[i]:
                    continue
                queue.append((subset + [nums[i]], i + 1))


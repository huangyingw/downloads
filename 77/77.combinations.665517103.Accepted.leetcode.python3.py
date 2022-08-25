#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (41.44%)
# Total Accepted:    143.5K
# Total Submissions: 346.3K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
# Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#
#


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(left, right, k):
            if k == 0:
                result.append(list(current))
            for index in range(left, right + 1):
                current.append(index)
                helper(index + 1, right, k - 1)
                current.pop()
        current = []
        result = []
        helper(1, n, k)
        return result


"""
Problem Link: https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x 
with a <= x <= b.  The intersection of two closed intervals is a set of real numbers 
that is either empty, or can be represented as a closed interval.  
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 
Note:
0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
      indexA = indexB = 0
      res = []
      while indexA < len(A) and indexB < len(B):
        # startpoint of the intersection
        start = max(A[indexA][0], B[indexB][0])
        # endpoint of the intersection
        end = min(A[indexA][1], B[indexB][1])
        # if A and B intersect
        if start <= end:
          res.append([start,end])
          
        # Remove the interval with the smallest endpoint
        if A[indexA][1] < B[indexB][1]:
          indexA += 1
        else:
          indexB += 1
      return res

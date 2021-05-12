"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.
Example 1:
Input: [1,2,3,3]
Output: 3
Example 2:
Input: [2,1,2,5,3,2]
Output: 2
Example 3:
Input: [5,1,5,2,5,3,5,4]
Output: 5
Note:
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
from collections import Counter


class Solution:

    def repeatedNTimes1(self, A):

        mapping = Counter(A)
        return mapping.most_common(1)[0][0]

    def repeatedNTimes2(self, A):
        lookup = set()
        for element in A:
            if element not in lookup:
                lookup.add(element)
            else:
                return element

    def repeatedNTimes3(self, A):

        import random
        i = 0
        j = 0
        while (A[i] != A[j] or i == j):
            i = random.randint(0, len(A) - 1)
            j = random.randint(0, len(A) - 1)
        return A[i]


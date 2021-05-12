class Solution:
    def isMonotonic(self, A):
        return A == sorted(B, reverse=True if A[0] > A[-1] else False)


class Solution:
    def isMonotonic(self, A):
        is_reverse = False
        if A[0] > A[-1]:
            is_reverse = True
        B = sorted(A, reverse=is_reverse)
        return A == B


class Solution(object):
    def sortArrayByParity(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            if A[lo] % 2 > A[hi] % 2:
                A[lo], A[hi] = A[hi], A[lo]
            elif A[lo] % 2 == 0:
                lo += 1
            elif A[hi] % 2 == 1:
                hi -= 1
        return A


class Solution(object):
    def sortArrayByParity(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] % 2 > A[r] % 2:
                A[l], A[r] = A[r], A[l]
            elif A[l] % 2 == 0:
                l += 1
            elif A[r] % 2 == 1:
                r -= 1
        return A


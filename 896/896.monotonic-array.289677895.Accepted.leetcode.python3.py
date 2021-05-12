class Solution:
    def isMonotonic(self, A):
        if not A or len(A) < 2:
            return True
        if A[0] <= A[-1]:
            left = A[0]
            for x in A:
                if x >= left:
                    left = x
                else:
                    return False
        else:
            left = A[0]
            for x in A:
                if x <= left:
                    left = x
                else:
                    return False
        return True


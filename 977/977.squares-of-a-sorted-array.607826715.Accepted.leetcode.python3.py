class Solution(object):
    def sortedSquares(self, A):

        N = len(A)
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1
        result = []
        while i >= 0 and j < N:
            if A[i]**2 < A[j]**2:
                result.append(A[i]**2)
                i -= 1
            else:
                result.append(A[j]**2)
                j += 1
        while i >= 0:
            result.append(A[i]**2)
            i -= 1
        while j < N:
            result.append(A[j]**2)
            j += 1
        return result


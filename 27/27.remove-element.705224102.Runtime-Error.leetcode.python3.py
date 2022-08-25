class Solution:
    def removeElement(self, A, elem):
        j = len(A) - 1
        for idx in reversed(len(A) - 1):
            if A[idx] == elem:
                A[idx], A[j] = A[j], A[idx]
                j -= 1
        return j + 1


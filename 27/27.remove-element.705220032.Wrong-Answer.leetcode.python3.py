class Solution:
    def removeElement(self, A, elem):
        j = len(A) - 1
        for i in reversed(range(len(A) - 1)):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j + 1


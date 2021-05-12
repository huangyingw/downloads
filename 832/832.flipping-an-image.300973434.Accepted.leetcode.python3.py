class Solution:
    def flipAndInvertImage(self, A):
        for r in range(len(A)):
            for c in range(len(A[0])):
                A[r][c] ^= 1
        for r in range(len(A)):
            A[r].reverse()
        return A


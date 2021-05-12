class Solution:

    def flipAndInvertImage(self, A):

        for r in range(len(A)):
            for c in range(len(A[0])):

                A[r][c] ^= 1
        for r in range(len(A)):
            A[r].reverse()
        return A

    def flipAndInvertImage(self, A):

        reverse = []
        for i in A:
            temp = []
            for j in reversed(i):
                if(j == 0):
                    temp.append(1)
                else:
                    temp.append(0)
            reverse.append(temp)
        return (reverse)


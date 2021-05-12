class Solution:

    def transpose(self, A):

        trans = []
        for c in range(len(A[0])):
            temp = []
            for r in range(len(A)):
                temp.append(A[r][c])
            trans.append(temp)
        return trans

    def transpose(self, A):
        M, N = len(A), len(A[0])
        trans = [[None for m in range(M)] for n in range(N)]
        for i in range(M):
            for j in range(N):
                trans[j][i] = trans[i][j]
        return trans


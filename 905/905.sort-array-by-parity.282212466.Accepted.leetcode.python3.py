class Solution(object):
    def sortArrayByParity(self, A):
        index = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[index], A[i] = A[i], A[index]
                index += 1
        return A


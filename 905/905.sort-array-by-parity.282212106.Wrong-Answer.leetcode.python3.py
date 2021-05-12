class Solution(object):
    def sortArrayByParity(self, A):
        index = 0
        for num in A:
            if num % 2 == 0:
                A[index], num = num, A[index]
                index += 1
        return A


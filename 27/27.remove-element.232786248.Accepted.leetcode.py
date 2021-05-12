class Solution:
    def removeElement(self, A, elem):
        index = 0
        for num in A:
            if num != elem:
                A[index] = num
                index += 1
        return index


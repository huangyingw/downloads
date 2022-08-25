class Solution:
    def removeElement(self, A, elem):
        j = len(A) - 1
        for num in reversed(A):
            print("num --> %s" % num)
            if num == elem:
                num, A[j] = A[j], num
                j -= 1
        print("A[%s] --> %s" % (j, A[j]))
        print("A --> %s" % A)
        return j + 1


class Solution:
    def removeElement(self, A, elem):
        j = len(A) - 1
        for num in reversed(A):
            print("num --> %s" % num)
            if num == elem:
                num, A[j] = A[j], num
                print("A --> %s" % A)
                j -= 1
        print("A[%s] --> %s" % (j, A[j]))
        return j + 1


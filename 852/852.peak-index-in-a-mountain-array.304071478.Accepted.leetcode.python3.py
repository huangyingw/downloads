class Solution(object):
    def peakIndexInMountainArray(self, A):
        first = 0
        last = len(A) - 1
        while first <= last:
            mid = (first + last) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1]:
                first = mid
            else:
                last = mid


class Solution(object):
    def peakIndexInMountainArray(self, A):
        first = 0
        last = len(A) - 1
        mid = (first + last) // 2
        while first <= last:
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1]:
                first = mid
            else:
                last = mid
            mid = (first + last) // 2


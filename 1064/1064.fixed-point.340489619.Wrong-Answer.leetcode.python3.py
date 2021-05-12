class Solution(object):
    def fixedPoint(self, A):
        left, right = 0, len(A)
        while left < right:
            mid = (left + right) // 2
            if A[mid] == mid:
                return mid
            if A[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return -1


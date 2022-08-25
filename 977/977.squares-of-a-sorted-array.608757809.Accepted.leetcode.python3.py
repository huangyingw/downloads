class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        right = 0
        while right < N and A[right] <= 0:
            right += 1
        left = right - 1
        result = []
        while left >= 0 and right < N:
            if A[left]**2 < A[right]**2:
                result.append(A[left]**2)
                left -= 1
            else:
                result.append(A[right]**2)
                right += 1
        while left >= 0:
            result.append(A[left]**2)
            left -= 1
        while right < N:
            result.append(A[right]**2)
            right += 1
        return result


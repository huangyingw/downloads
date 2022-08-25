class Solution:
    def sortedSquares(self, A):
        left, right = 0, len(A) - 1
        result = []
        while left <= right:
            if abs(A[left]) < abs(A[right]):
                result.append(A[left] * A[left])
                left += 1
            else:
                result.append(A[right] * A[right])
                right -= 1
        return result


class Solution:
    def sortedSquares(self, A):
        return [a ** 2 for a in sorted(A, key=lambda a: abs(a))]


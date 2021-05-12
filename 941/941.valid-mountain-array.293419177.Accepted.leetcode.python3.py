class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        if A[0] >= A[1]:
            return False
        climb = True
        for a, b in zip(A, A[1:]):
            if climb:
                if a < b:
                    continue
                if a > b:
                    climb = False
                    continue
                return False
            else:
                if a > b:
                    continue
                return False
        return not climb


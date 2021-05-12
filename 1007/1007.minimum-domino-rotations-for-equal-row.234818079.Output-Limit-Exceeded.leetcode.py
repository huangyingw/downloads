class Solution(object):
    def minDominoRotations(self, A, B):
        if len(A) != len(B):
            return -1
        if len(A) == 0:
            return 0

        for possibility in set([A[0], B[0]]):
            print('possibility --> %s' % possibility)
            top_rotation, bottom_rotation = 0, 0
            for a, b in zip(A, B):
                if possibility not in [a, b]:
                    break
                top_rotation += int(b != possibility)
                print('top_rotation --> %s' % top_rotation)
                bottom_rotation += int(a != possibility)
                print('bottom_rotation --> %s' % bottom_rotation)
            else:
                return min(top_rotation, bottom_rotation)
        return -1


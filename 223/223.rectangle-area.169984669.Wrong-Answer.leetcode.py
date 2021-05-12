class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        print('left --> %s' % left)
        right = min(C, G)
        print('right --> %s' % left)
        low = max(B, F)
        print('low --> %s' % low)
        hight = min(H, D)
        print('hight --> %s' % hight)
        return (C - A) * (D - B) + (G - E) * (H - F) - (right - left) * (hight - low)


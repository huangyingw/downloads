class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        right = min(C, G)
        low = max(B, F)
        hight = min(H, D)
        print('left --> %s' % left)
        print('low --> %s' % low)
        print('right --> %s' % right)
        print('hight --> %s' % hight)
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        share = (right - left) * (hight - low)
        print('area1 --> %s' % area1)
        print('area2 --> %s' % area2)
        print('share --> %s' % share)
        return area1 + area2 - share


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        right = min(C, G)
        low = max(B, F)
        hight = min(H, D)
        sums = (C - A) * (D - B) + (G - E) * (H - F)

        if left > right or low > hight:
            return sums

        return sums - (right - left) * (hight - low)


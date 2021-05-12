class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        right = min(C, G)
        low = max(B, F)
        hight = min(H, D)
        return (C - A) * (D - B) + (G - E) * (H - F) - (right - left) * (hight - low)


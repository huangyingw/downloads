class Solution:
    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            res = max(res, (r - l) * h)
            while height[l] <= h:
                l += 1
            while height[r] <= h:
                r -= 1
        return res


class Solution:
    def maxArea(self, height):
        ret = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                ret = max(ret, min(height[i], height[j]) * (j - i))
        return ret


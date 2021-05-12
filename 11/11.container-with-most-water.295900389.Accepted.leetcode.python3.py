class Solution:
    def maxArea(self, height):
        lpoint, rpoint = 0, len(height) - 1
        max_area = 0
        while lpoint < rpoint:
            max_area = max(max_area, (rpoint - lpoint) * min(height[rpoint], height[lpoint]))
            if height[rpoint] > height[lpoint]:
                lpoint += 1
            else:
                rpoint -= 1
        return max_area


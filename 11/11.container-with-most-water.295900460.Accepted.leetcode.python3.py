class Solution:
    def maxArea(self, height):
        max_container = 0
        pos_left, pos_right = 0, len(height) - 1
        while(pos_left < pos_right):
            if(height[pos_left] > height[pos_right]):
                max_container = max(max_container, (pos_right - pos_left) * height[pos_right])
                pos_right -= 1
            else:
                max_container = max(max_container, (pos_right - pos_left) * height[pos_left])
                pos_left += 1
        return max_container


class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            if height[left] < height[right]:
                result += (leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                result += (rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1
        return result


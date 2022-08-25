class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        result = leftMax = rightMax = 0
        while left < right:
            if height[left] < height[right]:
                result += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                result += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])
        return result


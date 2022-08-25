class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        result = leftMax = rightMax = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
        return result


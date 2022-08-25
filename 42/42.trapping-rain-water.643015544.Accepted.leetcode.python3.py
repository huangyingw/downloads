class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        result = leftMax = rightMax = 0
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                right -= 1
        return result


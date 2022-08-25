class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax = rightMax = result = 0
        while left < right:
            if leftMax < rightMax:
                result += max(0, leftMax - height[left])
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                result += max(0, rightMax - height[right])
                right -= 1
                rightMax = max(rightMax, height[right])
        return result


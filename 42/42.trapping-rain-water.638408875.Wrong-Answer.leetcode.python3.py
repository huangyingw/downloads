class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        result = leftMax = rightMax = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                result += max(0, (leftMax - height[left]))
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                result += max(0, (rightMax - height[right]))
                rightMax = max(rightMax, height[right])
        return result


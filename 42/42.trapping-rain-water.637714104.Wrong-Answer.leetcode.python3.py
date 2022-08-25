class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            if leftMax < rightMax:
                result += (leftMax - height[left])
                print("result --> %s" % result)
                left += 1
                leftMax = max(leftMax, left)
            else:
                result += (rightMax - height[right])
                print("result --> %s" % result)
                right -= 1
                rightMax = max(rightMax, height[right])
        return result


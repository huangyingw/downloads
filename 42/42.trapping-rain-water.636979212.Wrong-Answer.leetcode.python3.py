class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        result = 0
        while left < right:
            if leftMax < rightMax:
                result += max(0, (leftMax - height[left]))
                print("leftMax --> %s" % leftMax)
                print("height[%s] --> %s" % (left, height[left]))
                print("result --> %s" % result)
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                result += max(0, (rightMax - height[right]))
                print("rightMax --> %s" % rightMax)
                print("height[%s] --> %s" % (right, height[right]))
                print("result --> %s" % result)
                right -= 1
                rightMax = max(rightMax, height[right])
        return result


class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        result = leftMax = rightMax = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                print("leftMax --> %s" % leftMax)
                print("height[%s] --> %s" % (left, height[left]))
                result += max(0, (leftMax - height[left]))
                print("result --> %s" % result)
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                print("rightMax --> %s" % rightMax)
                print("height[%s] --> %s" % (right, height[right]))
                result += max(0, (rightMax - height[right]))
                print("result --> %s" % result)
                rightMax = max(rightMax, height[right])
        return result


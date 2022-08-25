class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            if leftMax < rightMax:
                print("leftMax --> %s" % leftMax)
                print("height[%s] --> %s" % (left, height[left]))
                result += (leftMax - height[left])
                print("result --> %s" % result)
                left += 1
                leftMax = max(leftMax, left)
            else:
                print("rightMax --> %s" % rightMax)
                print("height[%s] --> %s" % (right, height[right]))
                result += (rightMax - height[right])
                print("result --> %s" % result)
                right -= 1
                rightMax = max(rightMax, height[right])
        return result


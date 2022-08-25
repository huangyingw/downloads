class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                print("height[%s] --> %s" % (left, height[left]))
                leftMax = max(leftMax, height[left])
                result += (leftMax - height[left])
                print("result --> %s" % result)
                print("leftMax --> %s" % leftMax)
            else:
                right -= 1
                print("right --> %s" % right)
                print("height[%s] --> %s" % (right, height[right]))
                rightMax = max(rightMax, height[right])
                result += (rightMax - height[right])
                print("result --> %s" % result)
                print("rightMax --> %s" % rightMax)
        return result


class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left <= right:
            if leftMax < rightMax:
                print("height[%s] --> %s" % (left, height[left]))
                result += max(0, (leftMax - height[left]))
                print("result --> %s" % result)
                leftMax = max(leftMax, height[left])
                print("leftMax --> %s" % leftMax)
                left += 1
                print("left --> %s" % left)
            else:
                print("height[%s] --> %s" % (right, height[right]))
                result += max(0, (rightMax - height[right]))
                print("result --> %s" % result)
                rightMax = max(rightMax, height[right])
                print("rightMax --> %s" % rightMax)
                right -= 1
                print("right --> %s" % right)
        return result


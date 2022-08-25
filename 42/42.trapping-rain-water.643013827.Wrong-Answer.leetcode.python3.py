class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax = rightMax = result = 0
        while left < right:
            print("leftMax --> %s" % leftMax)
            print("rightMax --> %s" % rightMax)
            if leftMax < rightMax:
                result += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left += 1
                print("height[%s] --> %s" % (left, height[left]))
                print("result --> %s" % result)
            else:
                result += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1
                print("height[%s] --> %s" % (right, height[right]))
                print("result --> %s" % result)
        return result


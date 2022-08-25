class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                result += (leftMax - height[left])
                print("result --> %s" % result)
                print("left --> %s" % left)
                leftMax = max(leftMax, height[left])
                print("leftMax --> %s" % leftMax)
            else:
                right -= 1
                result += (rightMax - height[right])
                print("result --> %s" % result)
                print("right --> %s" % right)
                rightMax = max(rightMax, height[right])
                print("rightMax --> %s" % rightMax)
        return result


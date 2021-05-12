class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        while left < right:
            print()
            if leftMax < rightMax:
                result += (leftMax - height[left])
                print('result --> %s' % result)
                left += 1
                print('left --> %s' % left)
                leftMax = max(leftMax, left)
                print('leftMax --> %s' % leftMax)
            else:
                result += (rightMax - height[right])
                print('result --> %s' % result)
                right -= 1
                print('right --> %s' % right)
                rightMax = max(rightMax, height[right])
                print('rightMax --> %s' % rightMax)
        return result


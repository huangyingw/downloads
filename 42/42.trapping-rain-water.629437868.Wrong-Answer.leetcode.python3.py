class Solution:
    def trap(self, height):
        ans = current = 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            current += 1
            stack.append(current)
        return ans


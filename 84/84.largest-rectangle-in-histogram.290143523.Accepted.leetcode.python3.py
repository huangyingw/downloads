class Solution(object):
    def largestRectangleArea(self, heights):
        largest_rectangle = 0
        ls = len(heights)
        stack = [-1]
        top, pos = 0, 0
        for pos in range(ls):
            while top > 0 and heights[stack[top]] > heights[pos]:
                largest_rectangle = max(largest_rectangle, heights[stack[top]] * (pos - stack[top - 1] - 1))
                top -= 1
                stack.pop()
            stack.append(pos)
            top += 1
        while top > 0:
            largest_rectangle = max(largest_rectangle, heights[stack[top]] * (ls - stack[top - 1] - 1))
            top -= 1
        return largest_rectangle


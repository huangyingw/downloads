class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        heights = [0] * cols
        for row in range(rows):
            heights = [heights[i] + 1 if matrix[row][i] == '1' else 0 for i in range(cols)]
            heights.append(0)
            stack = [-1]
            for col in range(1, len(heights)):
                while heights[col] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = col - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(col)
        return max_area


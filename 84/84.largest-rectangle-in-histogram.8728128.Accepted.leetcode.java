public class Solution {
    public int largestRectangleArea(int[] height) {
      int maxArea = 0;
      Stack<Integer> stack = new Stack<Integer>();
      int i = 0;

      while (i < height.length) {
        if (stack.isEmpty() || height[stack.peek()] <= height[i]) {
          stack.push(i++);
        }
        else {
          int pos = stack.pop();
          maxArea = Math.max(maxArea,
                             (stack.isEmpty() ? i : i - stack.peek() - 1) * height[pos]);
        }
      }

      while (!stack.isEmpty()) {
        int pos = stack.pop();
        maxArea = Math.max(maxArea,
                           (stack.isEmpty() ? i : i - stack.peek() - 1) * height[pos]);
      }

      return maxArea;
    }
  }


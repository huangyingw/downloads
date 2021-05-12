  public class Solution
  {
    private int largestRectangleArea(int[] height)
    {
      Stack<Integer> stack = new Stack<Integer>();
      int i = 0;
      int maxArea = 0;
      int[] h = new int[height.length + 1];
      h = Arrays.copyOf(height, height.length + 1);

      while (i < h.length)
      {
        if (stack.isEmpty() || h[stack.peek()] <= h[i])
        {
          stack.push(i++);
        }
        else
        {
          int t = stack.pop();
          maxArea = Math.max(maxArea,
                             h[t] * (stack.isEmpty() ? i : i - stack.peek() - 1));
        }
      }

      return maxArea;
    }
    public int maximalRectangle(char[][] matrix)
    {
      if (matrix.length == 0 || matrix[0].length == 0)
      {
        return 0;
      }

      int m = matrix.length;
      int n = matrix[0].length;
      int[] height = new int[n + 1];
      int maxArea = 0;

      for (int i = 0; i < m; i++)
      {
        for (int j = 0; j < n; j++)
        {
          if (matrix[i][j] == '1')
          {
            height[j]++;
          }
          else
          {
            height[j] = 0;
          }
        }

        maxArea = Math.max(maxArea, largestRectangleArea(height));
      }

      return maxArea;
    }
  }


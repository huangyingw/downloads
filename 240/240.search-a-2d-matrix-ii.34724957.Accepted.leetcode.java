  public class Solution
  {
    public boolean searchMatrix(int[][] matrix, int target)
    {
      return dfs(matrix, 0, matrix.length - 1, 0, matrix[0].length - 1, target);
    }

    boolean dfs(int[][] matrix, int rowStart, int rowEnd, int colStart,
                int colEnd, int target)
    {
      if (rowStart > rowEnd || colStart > colEnd)
      {
        return false;
      }

      int rm = (rowStart + rowEnd) / 2, cm = (colStart + colEnd) / 2;

      if (matrix[rm][cm] == target)
      {
        return true;
      }
      else if (matrix[rm][cm] > target)
      {
        return dfs(matrix, rowStart, rm - 1, colStart, cm - 1, target)
          || dfs(matrix, rm, rowEnd, colStart, cm - 1, target)
          || dfs(matrix, rowStart, rm - 1, cm, colEnd, target);
      }
      else
      {
        return dfs(matrix, rm + 1, rowEnd, cm + 1, colEnd, target)
          || dfs(matrix, rm + 1, rowEnd, colStart, cm, target)
          || dfs(matrix, rowStart, rm, cm + 1, colEnd, target);
      }
    }
  }


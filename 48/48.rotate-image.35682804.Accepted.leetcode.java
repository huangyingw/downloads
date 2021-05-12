  public class Solution
  {
    public void rotate(int[][] matrix)
    {
      if (matrix == null)
      {
        return;
      }

      int n = matrix.length;
      int i, j;

      for (i = 0; i < n; i++)
      {
        for (j = 0; j < i; j++)
        {
          int tmp = matrix[i][j];
          matrix[i][j] = matrix[j][i];
          matrix[j][i] = tmp;
        }
      }

      for (i = 0; i < n; i++)
      {
        for (j = 0; j < n / 2; j++)
        {
          int tmp = matrix[i][n - 1 - j];
          matrix[i][n - 1 - j] = matrix[i][j];
          matrix[i][j] = tmp;
        }
      }
    }
  }


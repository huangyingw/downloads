  public class Solution
  {
    int result;

    public int totalNQueens(int n)
    {
      result = 0;

      if (n <= 0)
      {
        return result;
      }

      int[] columnForRow = new int[n];
      dfs(columnForRow, 0, n);
      return result;
    }

    public void dfs(int[] columnForRow, int row, int n)
    {
      if (row == n)
      {
        result += 1;
        return;
      }

      for (int i = 0; i < n; i++ )
      {
        columnForRow[row] = i;

        if (isValid(columnForRow, row))
        {
          dfs(columnForRow, row + 1, n);
        }
      }
    }

    public boolean isValid(int[] columnForRow, int row)
    {
      for (int i = 0; i < row; i++ )
      {
        if (columnForRow[i] == columnForRow[row] || Math.abs(columnForRow[i] - columnForRow[row]) == (row - i))
        {
          return false;
        }
      }

      return true;
    }
  }


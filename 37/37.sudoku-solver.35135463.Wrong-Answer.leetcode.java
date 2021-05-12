  public class Solution
  {
    private boolean isValid(char[][] board, int row, int column, char c)
    {
      for (int i = 0; i < 9; i++)
      {
        if (board[i][column] == c || board[row][i] == c
            || board[row - row % 3 + i / 3][column - column % 3 + i % 3] == c)
        {
          return false;
        }
      }

      return true;
    }

    private boolean dfs(char[][] board, int pos)
    {
      while (pos < 81 && board[pos / 9][pos % 9] != '.')
      {
        pos++ ;
      }

      if (pos == 81)
      {
        return true;
      }

      int row = pos / 9;
      int column = pos % 9;

      for (char c = '1'; c <= '9'; c++)
      {
        if (isValid(board, row, column, c))
        {
          board[row][column] = c;

          if (dfs(board, pos + 1))
          {
            return true;
          }
        }
      }

      return false;
    }

    public void solveSudoku(char[][] board)
    {
      dfs(board, 0);
    }
  }


  public class Solution
  {
    public void gameOfLife(int[][] board)
    {
      int m = board.length;
      int n = board[0].length;
      int[] dx = { -1, -1, 0, 1, 1, 1, 0, -1};
      int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

      for (int i = 0; i < m; i++)
      {
        for (int j = 0; j < n; j++)
        {
          int count = 0;

          for (int k = 0; k < 8; k++)
          {
            int x = i + dx[k];
            int y = j + dy[k];

            if (x >= 0 && x < m && y >= 0 && y < n && (board[x][y] & 1) == 1)
            {
              count++;
            }
          }

          if (count == 3 && (board[i][j] & 1) == 0)
          {
            board[i][j] = 2;
          }

          if (count < 2 && (board[i][j] & 1) == 0)
          {
            board[i][j] = 0;
          }

          if (count >= 2 && count <= 3 && (board[i][j] & 1) == 1)
          {
            board[i][j] = 3;
          }

          if (count > 3 && (board[i][j] & 1) == 1)
          {
            board[i][j] = 1;
          }
        }
      }

      for (int i = 0; i < m; i++)
      {
        for (int j = 0; j < n; j++)
        {
          board[i][j] >>= 1;
        }
      }
    }
  }


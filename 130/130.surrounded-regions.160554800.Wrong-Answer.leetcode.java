public class Solution
{
    private class Pos
    {
        int x;
        int y;

        Pos(int x, int y)
        {
            this.x = x;
            this.y = y;
        }
    }

    private boolean isOutOfBound(int x, int y, int rows, int columns)
    {
        return x < 0 || y < 0 || x >= rows || y >= columns;
    }

    public void solve(char[][] board)
    {
        if (board.length == 0 || board[0].length == 0)
        {
            return;
        }

        int rows = board.length;
        int columns = board[0].length;
        LinkedList<Pos> queue = new LinkedList<Pos>();

        for (int i = 0; i < rows; i++)
        {
            queue.add(new Pos(i, 0));
            queue.add(new Pos(i, columns - 1));
        }

        for (int i = 0; i < columns; i++)
        {
            queue.add(new Pos(0, i));
            queue.add(new Pos(rows - 1, i));
        }

        while (!queue.isEmpty())
        {
            Pos pos = queue.remove();
            int x = pos.x;
            int y = pos.y;

            if (isOutOfBound(x, y, rows, columns) || board[x][y] != 'O')
            {
                continue;
            }

            board[x][y] = 'N';
        }

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < columns; j++)
            {
                if (board[i][j] == 'O')
                {
                    board[i][j] = 'X';
                }
                else if (board[i][j] == 'N')
                {
                    board[i][j] = 'O';
                }
            }
        }
    }
}


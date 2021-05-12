public class Solution
{
    public boolean isValidSudoku(char[][] board)
    {
        for (int i = 0; i < board[0].length; i++)
        {
            HashSet<Character> test = new HashSet<Character>();

            for (int j = 0; j < board.length; j++)
            {
                if (board[j][i] != '.' && !test.add(board[j][i]))
                {
                    return false;
                }
            }
        }

        for (int i = 0; i < board.length; i++)
        {
            HashSet<Character> test = new HashSet<Character>();

            for (int j = 0; j < board[0].length; j++)
            {
                if (board[i][j] != '.' && !test.add(board[i][j]))
                {
                    return false;
                }
            }
        }

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++) // for each sub-box
            {
                HashSet<Character> test = new HashSet<Character>();
            }
        }

        return true;
    }
}

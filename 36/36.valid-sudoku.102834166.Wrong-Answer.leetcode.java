public class Solution
{
    public boolean isValidSudoku(char[][] board)
    {
        for (int i = 0; i < board[0].length; i++)
        {
            HashSet<Character> test = new HashSet<Character>();

            for (int j = 0; j < board.length; j++)
            {
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

                for (int m = i * 3; m < i * 3 + 3; m++) //row
                {
                    for (int n = j * 3; n < j * 3 + 3; n++) //column
                    {
                        if (board[m][n] != '.' && !test.add(board[m][n]))
                        {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}

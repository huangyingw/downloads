public class Solution
{
    private boolean dfs(char[][] board, boolean[][] visited, int i, int j, String word, int begin)
    {
        if (begin == word.length())
        {
            return true;
        }

        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || visited[i][j] || board[i][j] != word.charAt(begin))
        {
            return false;
        }

        visited[i][j] = true;
        boolean re = dfs(board, visited, i + 1, j, word, begin + 1)
                     || dfs(board, visited, i - 1, j, word, begin + 1)
                     || dfs(board, visited, i, j + 1, word, begin + 1)
                     || dfs(board, visited, i, j - 1, word, begin + 1);
        visited[i][j] = false;
        return re;
    }

    public boolean exist(char[][] board, String word)
    {
        boolean[][] visited = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++)
        {
            for (int j = 0; j < board[0].length; j++)
            {
                if (dfs(board, visited, i, j, word, 0))
                {
                    return true;
                }
            }
        }

        return false;
    }
}


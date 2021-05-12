public class Solution
{
    private int m, n;
    public int numIslands(char[][] grid)
    {
        if(grid == null || grid.length == 0)
        {
            return 0;    
        }
        
        m = grid.length;
        n = grid[0].length;
        int result = 0;

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] != '1')
                {
                    continue;
                }

                result++ ;
                dfs(grid, i, j);
            }
        }

        return result;
    }
    
    public void dfs(char[][] grid, int i, int j)
    {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0')
        {
            return;
        }
        
        grid[i][j] = '0';
        dfs(grid, i - 1, j);
        dfs(grid, i + 1, j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }
}

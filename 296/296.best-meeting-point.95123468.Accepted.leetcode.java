public class Solution
{
    public int minTotalDistance(int[][] grid)
    {
        int m = grid.length;
        int n = grid[0].length;
        ArrayList<Integer> cols = new ArrayList<Integer>();
        ArrayList<Integer> rows = new ArrayList<Integer>();

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 1)
                {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        
        Collections.sort(cols);
        int sum = 0;
        
        for (int i = 0; i < rows.size(); i++)
        {
            sum += Math.abs(rows.get(i) - rows.get(rows.size() / 2));
        }
        
        for (int i = 0; i < cols.size(); i++)
        {
            sum += Math.abs(cols.get(i) - cols.get(cols.size() / 2));
        }
        
        return sum;
    }
}

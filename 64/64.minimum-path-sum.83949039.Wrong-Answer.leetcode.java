public class Solution 
{
    public int minPathSum(int[][] grid) 
    {
        if(grid[0].length == 1)
        {
            return grid[0][0];    
        }
        
		int[] dp = new int[grid[0].length + 1];
		Arrays.fill(dp, Integer.MAX_VALUE);
		dp[0] = 0;
		dp[1] = grid[0][0];

        for (int i = 0; i < grid.length; i++) 
        {
            dp[1] += grid[i][0];
            
		    for (int j = 2; j <= grid[0].length; j++) 
		    {
			    dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j - 1];
			}
		}

		return dp[grid[0].length];
	}
}

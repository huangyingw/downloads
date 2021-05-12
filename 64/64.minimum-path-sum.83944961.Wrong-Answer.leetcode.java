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
		
        for (int i = 0; i < grid.length; i++) 
        {
		    for (int j = 1; j <= grid[0].length; j++) 
		    {
			    dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j - 1];
			}
		}

		return dp[grid[0].length];
	}
}

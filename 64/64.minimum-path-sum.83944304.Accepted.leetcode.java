public class Solution 
{
    public int minPathSum(int[][] grid) 
    {
        int[] dp = new int[grid[0].length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < grid.length; i++) 
        {
            dp[0] += grid[i][0];

            for (int j = 1; j < grid[0].length; j++) 
            {
                dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }

        return dp[grid[0].length - 1];
    }
}

public class Solution
{
    public int uniquePathsWithObstacles(int[][] data)
    {
        int m = data.length;
        int n = data[0].length;
        int[] dp = new int[n];
        dp[0] = 1;

        for (int i = 0; i < m; i++)
        {
            dp[0] = data[i][0] == 1 ? 0 : dp[0];
            
            for(int j = 1; j < n; j++)
            {
                dp[j] = data[i][0] == 1 ? 0 : dp[j] + dp[j - 1];
            }
        }

        return dp[n - 1];
    }
}

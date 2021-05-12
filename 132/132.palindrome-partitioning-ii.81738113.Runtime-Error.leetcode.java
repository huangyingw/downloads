public class Solution
{
    public int minCut(String s)
    {
        int n = s.length();
        int[] dp = new int[n];
        boolean isPalin[][] = new boolean[n][n];

        for (int i = 0; i < n; i++ )
        {
            dp[i] = n - 1 - i;
        }

        for (int i = n - 1; i >= 0; i-- )
        {
            for (int j = i; j < n; j++ )
            {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || isPalin[i + 1][j - 1]))
                {
                    isPalin[i][j] = true;
                    dp[i] = Math.min(dp[i], dp[j + 1] + 1);
                }
            }
        }

        return dp[0];
    }
}

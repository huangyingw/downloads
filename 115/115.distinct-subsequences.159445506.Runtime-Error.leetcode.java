public class Solution
{
    public int numDistinct(String S, String T)
    {
        int[][] dp = new int[S.length()][T.length()];

        for (int i = 0; i < S.length(); i++)
        {
            for (int j = 0; j < T.length(); j++)
            {
                if (i == 0 && j == 0)
                {
                    dp[i][j] = S.charAt(0) == T.charAt(0) ? 1 : 0;
                    continue;
                }

                dp[i][j] = dp[i - 1][j];

                if (S.charAt(i) == T.charAt(j))
                {
                    dp[i][j] += dp[i - 1][j - 1];
                }
            }
        }

        return dp[S.length() - 1][T.length() - 1];
    }
}


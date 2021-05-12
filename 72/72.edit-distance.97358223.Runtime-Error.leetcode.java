public class Solution
{
    public int minDistance(String word1, String word2)
    {
        int[][] dp = new int[word1.length()][word2.length()];

        dp[0][0] = word1.charAt(0) == word2.charAt(0) ? 0 : 1;
        
        for (int i = 1; i < word1.length(); i++)
        {
            for (int j = 1; j < word2.length(); j++)
            {
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                {
                    dp[i][j] = dp[i - 1][j - 1];
                    //System.out.println(i + "," + j + " --> " + dp[i][j]);
                }
                else
                {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]) + 1;
                    //System.out.println(i + "," + j + " --> " + dp[i][j]);
                }
            }
        }

        return dp[word1.length() - 1][word2.length() - 1];
    }
}

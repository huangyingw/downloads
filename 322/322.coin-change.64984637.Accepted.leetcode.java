  public class Solution
  {
    public int coinChange(int[] coins, int amount)
    {
      int dp[] = new int[amount + 1];
      final int INF = 0x7fffffff;

      for (int i = 1; i <= amount; i++)
      {
        dp[i] = INF;
      }

      for (int i = 0; i <= amount; i++)
      {
        for (int j = 0; j < coins.length; j++)
        {
          if (i + coins[j] <= amount && dp[i] != INF)
          {
            dp[i + coins[j]] = Math.min(dp[i + coins[j]], dp[i] + 1);
          }
        }
      }

      return dp[amount] == INF ? -1 : dp[amount];
    }
  }


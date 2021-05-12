  public class Solution
  {
    public int countNumbersWithUniqueDigits(int n)
    {
      n = Math.min(n, 10);
      int[] dp = new int[n + 1];
      dp[0] = 1;

      for (int i = 1; i <= n; i++)
      {
        dp[i] = 9;

        for (int x = 9; x >= 9 - i + 2; x--)
        {
          dp[i] *= x;
        }
      }

      int ans = 0;

      for (int i = 0; i < dp.length; i++)
      {
        ans += dp[i];
      }

      return ans;
    }
  }


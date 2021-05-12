  public class Solution
  {
    public boolean isMatch(String s, String p)
    {
      boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
      dp[0][0] = true;

      for (int i = 1; i <= s.length(); i++)
      {
        dp[i][0] = false;
      }

      for (int j = 1; j <= p.length(); j++)
      {
        dp[0][j] = j > 1 && p.charAt(j - 1) == '*' && dp[0][j - 2];
      }

      for (int i = 0; i < s.length(); i++)
      {
        for (int j = 0; j < p.length(); j++)
        {
          if (p.charAt(j) != '*')
          {
            dp[i + 1][j + 1] = (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)) && dp[i][j];
          }
          else
          {
            dp[i + 1][j + 1] = j > 0 && dp[i + 1][j - 1] || dp[i + 1][j]
                               || j > 0 && (p.charAt(j - 1) == '.' || s.charAt(i) == p.charAt(j - 1)) && dp[i][j + 1];
          }
        }
      }

      return dp[s.length()][p.length()];
    }
  }


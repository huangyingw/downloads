public class Solution
{
    public int numDecodings(String s)
    {
        if (s == null || s.isEmpty())
        {
            return 0;
        }

        int[] dp = new int[s.length() + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '0' ? 0 : 1;

        for (int i = 1; i < s.length(); i++)
        {
            if (s.charAt(i) != '0')
            {
                dp[i + 1] += dp[i];
            }

        }

        return dp[s.length()];
    }
}

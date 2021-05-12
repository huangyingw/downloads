public class Solution
{
    public boolean wordBreak(String s, List<String> dict)
    {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for (int start = 0; start < s.length(); start++)
        {
            if (!dp[start])
            {
                continue;
            }

            for (int end = start + 1; end <= s.length() && !dp[end]; end++)
            {
                dp[end] = dict.contains(s.substring(start, end));
            }
        }

        return dp[s.length()];
    }
}


public class Solution
{
    public String longestPalindrome(String s)
    {
        if (s == null || s.length() == 0)
        {
            return "";
        }

        boolean[][] dp = new boolean[s.length()][s.length()];
        String res = "";
        int maxLen = 0;

        for (int left = s.length() - 1; left >= 0; left--)
        {
            for (int right = left; right < s.length(); right++)
            {
                if (s.charAt(left) == s.charAt(right) && (right - left <= 2 || dp[left + 1][right - 1]))
                {
                    dp[left][right] = true;

                    if (maxLen < right - left + 1)
                    {
                        maxLen = right - left + 1;
                        res = s.substring(left, right + 1);
                    }
                }
            }
        }

        return res;
    }
}

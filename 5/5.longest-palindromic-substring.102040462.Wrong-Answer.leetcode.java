public class Solution
{
    public String longestPalindrome(String s)
    {
        if (s == null || s.length() == 0)
        {
            return "";
        }

        boolean[][] palin = new boolean[s.length()][s.length()];
        String res = "";
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++)
        {
            for (int j = i; j < s.length(); j++)
            {
                if (s.charAt(i) == s.charAt(j) && (j - i <= 2 || palin[i + 1][j - 1]))
                {
                    palin[i][j] = true;

                    if (maxLen < j - i + 1)
                    {
                        maxLen = j - i + 1;
                        res = s.substring(i, j + 1);
                    }
                }
            }
        }

        return res;
    }
}

public class Solution
{
    public String longestPalindrome(String s)
    {
        int len = s.length();
        Boolean[][] P = new Boolean[len][len];
        int maxL = 0, start = 0, end = 0;

        for (int i = 0; i < s.length(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                P[j][i] = (s.charAt(j) == s.charAt(i) && (i - j < 2 || P[j + 1][i - 1]));

                if (P[j][i] && maxL < (i - j + 1))
                {
                    maxL = i - j + 1;
                    start = j;
                    end = i;
                }
            }

            P[i][i] = true;
        }

        return s.substring(start, end - start + 1);
    }
}

public class Solution
{
    public boolean isOneEditDistance(String s, String t)
    {
        if (Math.abs(t.length() - s.length()) > 1)
        {
            return false;
        }

        if (s.length() > t.length())
        {
            return dfs(t, s);
        }

        return dfs(s, t);
    }
    private boolean dfs(String s, String t)
    {
        boolean has = false;

        for (int i = 0, j = 0; i < s.length(); ++i, ++j)
        {
            if (s.charAt(i) != t.charAt(j))
            {
                has = true;

                if (s.length() < t.length())
                {
                    --i;
                }
            }
        }

        return has || s.length() < t.length();
    }
}


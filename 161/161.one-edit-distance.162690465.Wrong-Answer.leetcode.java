public class Solution
{
    public boolean isOneEditDistance(String s, String t)
    {
        if (s.length() > t.length())
        {
            return helper(t, s);
        }

        return helper(s, t);
    }
    private boolean helper(String s, String t)
    {
        boolean has = false;

        for (int i = 0, j = 0; i < s.length(); ++i, ++j)
        {
            if (s.charAt(i) != t.charAt(j))
            {
                if (has)
                {
                    return false;
                }

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


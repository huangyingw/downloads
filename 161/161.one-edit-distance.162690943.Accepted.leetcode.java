public class Solution
{
    public boolean isOneEditDistance(String s, String t)
    {
        int m = s.length(), n = t.length();

        if (m > n)
        {
            return isOneEditDistance(t, s);
        }

        if (n - m > 1)
        {
            return false;
        }

        int i = 0, shift = n - m;

        while (i < m && s.charAt(i) == t.charAt(i))
        {
            ++i;
        }

        if (shift == 0)
        {
            i++;
        }

        while (i < m && s.charAt(i) == t.charAt(i + shift))
        {
            i++;
        }

        return i == m;
    }
}


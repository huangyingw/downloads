public class Solution
{
    public int firstUniqChar(String s)
    {
        char[] chs = s.toCharArray();
        Set<Character> m = new HashSet<Character>();

        for (int i = 0; i < chs.length; ++i)
        {
            m.add(chs[i]);
        }

        for (int i = 0; i < chs.length; ++i)
        {
            if (!m.contains(chs[i]))
            {
                return i;
            }
        }

        return 0;
    }
}

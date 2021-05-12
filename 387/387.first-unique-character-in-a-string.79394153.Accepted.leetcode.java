public class Solution
{
    public int firstUniqChar(String s)
    {
        char[] chs = s.toCharArray();
        Map<Character, Integer> m = new HashMap<Character, Integer>();

        for (char c : chs)
        {
            if(!m.containsKey(c))
            {
                m.put(c, 0);
            }
            
            m.put(c, m.get(c) + 1);
        }

        for (int i = 0; i < chs.length; ++i)
        {
            if (m.get(chs[i]) == 1)
            {
                return i;
            }
        }

        return -1;
    }
}

public class Solution
{
    public boolean isAnagram(String s, String t)
    {
        if (null == s || null == t || s.length() != t.length())
        {
            return false;
        }

        Map<Character, Integer> map = new HashMap<Character, Integer>();

        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);

            if (!map.containsKey(c))
            {
                map.put(c, 0);
            }

            map.put(c, map.get(c) + 1);
        }

        for (int i = 0; i < t.length(); i++)
        {
            char c = t.charAt(i);

            if (map.containsKey(c) && map.get(c) > 0)
            {
                map.put(c, map.get(c) - 1);
            }
            else
            {
                return false;
            }
        }

        for (Integer value : map.values())
        {
            if (value != 0)
            {
                return false;
            }
        }

        return true;
    }
}

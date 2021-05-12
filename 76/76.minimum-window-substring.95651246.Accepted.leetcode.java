public class Solution
{
    public String minWindow(String s, String t)
    {
        if (t.length() > s.length())
        {
            return "";
        }

        String result = "";
        HashMap<Character, Integer> target = new HashMap<Character, Integer>();

        for (int i = 0; i < t.length(); i++)
        {
            char c = t.charAt(i);

            if (!target.containsKey(c))
            {
                target.put(c, 0);
            }

            target.put(c, target.get(c) + 1);
        }

        // character counter for s
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int start = 0;
        int minLen = s.length() + 1;
        int count = 0; // the total of mapped characters

        for (int end = 0; end < s.length(); end++)
        {
            char c = s.charAt(end);

            if (target.containsKey(c))
            {
                if (map.containsKey(c))
                {
                    if (map.get(c) < target.get(c))
                    {
                        count++;
                    }

                    map.put(c, map.get(c) + 1);
                }
                else
                {
                    map.put(c, 1);
                    count++;
                }
            }

            if (count == t.length())
            {
                char sc = s.charAt(start);

                while (!map.containsKey(sc) || map.get(sc) > target.get(sc))
                {
                    if (map.containsKey(sc))
                    {
                        map.put(sc, map.get(sc) - 1);    
                    }
                    
                    sc = s.charAt(++start);
                }

                if (end - start + 1 < minLen)
                {
                    minLen = end - start + 1;
                    result = s.substring(start, end + 1);
                }
            }
        }

        return result;
    }
}

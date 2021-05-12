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
        HashMap<Character, Integer> source = new HashMap<Character, Integer>();
        int start = 0;
        int minLen = s.length() + 1;
        int count = 0; // the total of mapped characters

        for (int end = 0; end < s.length(); end++)
        {
            char c = s.charAt(end);

            if (target.containsKey(c))
            {
                if (source.containsKey(c))
                {
                    if (source.get(c) < target.get(c))
                    {
                        count++;
                    }

                    source.put(c, source.get(c) + 1);
                }
                else
                {
                    source.put(c, 1);
                    count++;
                }
            }

            if (count == t.length())
            {
                char sc = s.charAt(start);
                System.out.println("sc --> " + sc);
                System.out.println("source.get(sc) --> " + source.get(sc));
                System.out.println("target.get(sc) --> " + target.get(sc));

                while (!source.containsKey(sc) || source.get(sc) > target.get(sc))
                {
                    if (source.containsKey(sc))
                    {
                        source.put(sc, source.get(sc) - 1);    
                    }
                    
                    sc = s.charAt(++start);
                    System.out.println("sc --> " + sc);
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

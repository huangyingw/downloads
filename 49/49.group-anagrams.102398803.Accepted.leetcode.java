public class Solution
{
    public List<List<String>> groupAnagrams(String[] strs)
    {
        Map<String, List<String>> dict = new HashMap<String, List<String>>();

        for (String str : strs)
        {
            char[] cs = str.toCharArray();
            Arrays.sort(cs);
            String anagram = new String(cs);
            List<String> l = dict.get(anagram);

            if (l == null)
            {
                l = new ArrayList<String>();
                dict.put(anagram, l);
            }

            l.add(str);
        }

        return new ArrayList<List<String>>(dict.values());
    }
}

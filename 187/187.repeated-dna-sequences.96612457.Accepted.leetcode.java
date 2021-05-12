public class Solution
{
    public List<String> findRepeatedDnaSequences(String s)
    {
        Set<String> res = new HashSet<String>();
        Set<String> set = new HashSet<String>();

        for (int index = 10; index <= s.length(); index++)
        {
            String substr = s.substring(index - 10, index);

            if (set.contains(substr))
            {
                res.add(substr);
            }
            else
            {
                set.add(substr);
            }
        }

        return new ArrayList(res);
    }
}

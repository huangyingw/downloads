public class Solution
{
    public boolean isIsomorphic(String s, String t)
    {
        HashMap<Character, Character> sourceMap = new HashMap<Character, Character>();
        HashMap<Character, Character> targetMap = new HashMap<Character, Character>();

        for (int i = 0; i < s.length(); i++)
        {
            Character source = sourceMap.get(t.charAt(i));
            Character target = targetMap.get(s.charAt(i));

            if (source != null && target != null)
            {
                sourceMap.put(t.charAt(i), s.charAt(i));
                targetMap.put(s.charAt(i), t.charAt(i));
            }
            else if (target != t.charAt(i) || source != s.charAt(i))
            {
                return false;
            }
        }

        return true;
    }
}


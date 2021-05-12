public class Solution 
{
    public boolean isSubsequence(String s, String t) 
    {
        char[] ss = s.toCharArray();
        char[] tt = t.toCharArray();
        
        int i = 0;
        for (int j = 0; i < ss.length && j < tt.length; j++)
        {
            if (ss[i] == tt[j])
            {
                i++;
            }
        }
        
        return i == ss.length;
    }
}

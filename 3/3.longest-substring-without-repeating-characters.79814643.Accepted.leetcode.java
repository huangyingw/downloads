public class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
        if(s == null || s.length() == 0)    
        {
            return 0;
        }
        
        int[] map = new int[256];
        int left = 0,right = 0, ans = 0;
        
        while(right < s.length())
        {
            while(right < s.length() && map[s.charAt(right)] == 0)
            {
                map[s.charAt(right)] = 1;
                ans = Math.max(ans, right - left + 1);
                right++;
            }
            
            map[s.charAt(left++)] = 0;
        }
        
        return ans;
    }
}

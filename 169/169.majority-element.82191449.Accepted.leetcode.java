public class Solution 
{
    public int majorityElement(int[] num) 
    {
        int count = 1;
        int result = Integer.MAX_VALUE;
        
        for(int i = 0; i < num.length; i++) 
        {
            if(result == num[i]) 
            {
                count++;
            }
            else 
            {
                count--;
            }
            
            if(count == 0) 
            {
                result = num[i];
                count++;
            }
        }
        
        return result;
    }
}

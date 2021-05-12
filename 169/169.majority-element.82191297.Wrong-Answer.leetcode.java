public class Solution 
{
    public int majorityElement(int[] num) 
    {
        if(num.length == 1) 
        {
            return num[0];
        }
        
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
            }
        }
        
        return result;
    }
}

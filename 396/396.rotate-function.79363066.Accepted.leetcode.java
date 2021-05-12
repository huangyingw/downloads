public class Solution 
{
    public int maxRotateFunction(int[] A) 
    {  
        int max=Integer.MIN_VALUE;  
        int sum = 0;  
        int pre = 0;  
      
        for(int i=0;i<A.length;i++) 
        {  
            pre +=A[i]*i;  
            sum+=A[i];  
        }  
        
        max = Math.max(pre, max);  
  
        int k=1;  
        while(k<A.length) 
        {  
            int res = pre+sum-A.length*A[A.length-k];  
            max = Math.max(max, res);  
            pre = res;  
            k++;  
        }  
      
        return max;  
    } 
}

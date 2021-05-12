public class Solution 
{
    public int numberOfArithmeticSlices(int[] A) 
    {
        if (A == null || A.length < 3)
        {
            return 0;    
        }
        
        int[] dp = new int[A.length];
        int ans = 0;
        
        for (int i = 2; i < A.length; i++) 
        {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) 
            {
                dp[i] = dp[i - 1] + 1;
            }
        
            ans += dp[i];
        }
    
        return ans;
    }
}

public class Solution
{
    public int maxSubArray(int[] A)
    {
        int local = A[0];
        int global = A[0];

        for (int i = 1; i < A.length; i++)
        {
            local = Math.max(A[i], local + A[i]);
            global = Math.max(global, local);
        }
        
        return global;
    }
}

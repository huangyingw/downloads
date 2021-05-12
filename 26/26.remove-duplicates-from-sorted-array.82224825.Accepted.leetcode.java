public class Solution 
{
    public int removeDuplicates(int[] A) 
    {
        int index = 0;
    
        for(int nav = 1; nav < A.length; nav++)
        {
            if(A[nav] != A[index])   
            {
                A[++index] = A[nav];
            }
        }
    
        return index + 1;
    }
}

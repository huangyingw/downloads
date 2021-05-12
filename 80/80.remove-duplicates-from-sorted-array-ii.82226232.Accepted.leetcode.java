public class Solution 
{
    public int removeDuplicates(int[] A) 
    {
        if (A.length <= 2) 
        {
            return A.length;
        }

        int index = 2;

        for (int nav = 2; nav < A.length; nav++) 
        {
            if (A[nav] != A[index - 2]) 
            {
                A[index++] = A[nav];
            }
        }

        return index;
    }
}

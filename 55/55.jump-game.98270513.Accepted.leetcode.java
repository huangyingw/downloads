public class Solution
{
    public boolean canJump(int[] A)
    {
        int maxD = 0;
 
        for (int index = 0; index <= maxD && index < A.length; index++)
        {
            if (maxD >= A.length - 1)
            {
                return true;
            }

            maxD = Math.max(maxD, index + A[index]);
        }

        return false;
    }
}

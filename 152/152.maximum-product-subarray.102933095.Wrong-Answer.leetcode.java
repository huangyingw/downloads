public class Solution
{
    public int maxProduct(int[] A)
    {
        if (A.length == 0)
        {
            return 0;
        }

        int maxHere, minHere;
        int maxPre = A[0];
        int minPre = A[0];
        int maxNow = A[0];

        for (int i = 1; i < A.length; i++)
        {
            maxHere = Math.max(Math.max(maxPre * A[i], minPre * A[i]), A[i]);
            minHere = Math.min(Math.min(maxPre * A[i], minPre * A[i]), A[i]);
            maxNow = Math.max(maxNow, maxHere);
        }

        return maxNow;
    }
}

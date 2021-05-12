public class Solution
{
    public int maxProduct(int[] A)
    {
        if (A.length == 0)
        {
            return 0;
        }

        int maxHere, minHere;
        int maxPre = 0;
        int minPre = 0;
        int maxNow = 0;

        for (int i = 1; i < A.length; i++)
        {
            maxHere = Math.max(Math.max(maxPre * A[i], minPre * A[i]), A[i]);
            minHere = Math.min(Math.min(maxPre * A[i], minPre * A[i]), A[i]);
            maxPre = maxHere;
            minPre = minHere;
            maxNow = Math.max(maxNow, maxHere);
        }

        return maxNow;
    }
}

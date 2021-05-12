public class Solution
{
    public int removeDuplicates(int[] A)
    {
        int index = 1;

        for (int nav = 0; nav < A.length; nav++)
        {
            if (A[nav] != A[index - 1])
            {
                A[index++] = A[nav];
            }
        }

        return index;
    }
}


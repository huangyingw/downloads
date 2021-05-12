public class Solution
{
    public int removeDuplicates(int[] A)
    {
        int index = 2;

        for (int nav = 3; nav < A.length; nav++)
        {
            if (A[nav] != A[index - 2])
            {
                A[index++] = A[nav];
            }
        }

        return index;
    }
}


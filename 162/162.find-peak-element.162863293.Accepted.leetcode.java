class Solution
{
    public int findPeakElement(int[] A)
    {
        int start = 0, end = A.length - 1;

        while (start + 1 <  end)
        {
            int mid = (start + end) / 2;

            if (A[mid - 1] > A[mid])
            {
                end = mid;
            }
            else if (A[mid] < A[mid + 1])
            {
                start = mid;
            }
            else
            {
                end = mid;
            }
        }

        return A[start] < A[end] ? end : start;
    }
}


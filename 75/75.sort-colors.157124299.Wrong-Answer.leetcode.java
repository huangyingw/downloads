public class Solution
{
    public void sortColors(int[] A)
    {
        if (A == null)
        {
            return;
        }

        int redIndex = 0;
        int blueIndex = A.length - 1;
        int index = 0;

        while (index < blueIndex)
        {
            if (A[index] == 0)
            {
                swap(A, index++, redIndex++);
            }
            else if (A[index] == 2)
            {
                swap(A, index, blueIndex--);
            }
            else
            {
                index++;
            }
        }
    }

    private void swap(int[] a, int index, int blueIndex)
    {
        int temp = a[index];
        a[index] = a[blueIndex];
        a[blueIndex] = temp;
    }
}


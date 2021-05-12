public class Solution
{
    public int majorityElement(int[] num)
    {
        int count = 0;
        int result = Integer.MAX_VALUE;

        for (int i = 0; i < num.length; i++)
        {
            if (count == 0)
            {
                result = num[i];
            }

            if (result == num[i])
            {
                count++;
            }
            else
            {
                count--;
            }
        }

        return result;
    }
}


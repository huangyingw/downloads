public class Solution
{
    public int majorityElement(int[] nums)
    {
        int count = 0;
        int result = nums[0];

        for (int num : nums)
        {
            if (count == 0)
            {
                result = num;
            }

            if (result == num)
            {
                count++ ;
            }
            else
            {
                count-- ;
            }
        }

        return result;
    }
}


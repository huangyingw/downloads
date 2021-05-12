public class Solution
{
    public int majorityElement(int[] nums)
    {
        int result = nums[0];
        int count = 0;

        for (int nav = 1; nav < nums.length; nav++)
        {
            if (nums[nav] == result)
            {
                count++;
            }
            else
            {
                count--;

                if (count == 0)
                {
                    result = nums[nav];
                    count = 1;
                }
            }
        }

        return result;
    }
}


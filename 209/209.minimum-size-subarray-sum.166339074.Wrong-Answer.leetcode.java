public class Solution
{
    public int minSubArrayLen(int s, int[] nums)
    {
        int result = nums.length;
        int start = 0;
        int sum = 0;
        int i = 0;

        while (i <= nums.length)
        {
            if (sum >= s)
            {
                if (start == i - 1)
                {
                    return 1;
                }

                result = Math.min(result, i - start);
                sum = sum - nums[start];
                start++;
            }
            else
            {
                if (i == nums.length)
                {
                    break;
                }

                sum = sum + nums[i];
                i++;
            }
        }

        return result;
    }
}


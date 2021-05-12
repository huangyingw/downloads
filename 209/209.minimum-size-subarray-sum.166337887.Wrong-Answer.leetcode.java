public class Solution
{
    public int minSubArrayLen(int s, int[] nums)
    {
        int left = 0, right = 0, sum = 0;
        int min = Integer.MAX_VALUE;

        while (right < nums.length)
        {
            if (sum < s)
            {
                sum += nums[right++];
                System.out.printf("nums[right --> %s]--> %s\n", right - 1, nums[right - 1]);
                System.out.printf("sum--> %s\n", sum);
            }

            if (sum >= s)
            {
                min = Math.min(min, right - left);
                System.out.printf("min--> %s\n", min);
                sum -= nums[left++];
                System.out.printf("nums[left --> %s]--> %s\n", left - 1, nums[left - 1]);
                System.out.printf("sum--> %s\n", sum);
            }
        }

        return min == Integer.MAX_VALUE ? 0 : min;
    }
}


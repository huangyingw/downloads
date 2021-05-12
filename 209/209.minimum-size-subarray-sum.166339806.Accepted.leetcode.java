public class Solution
{
    public int minSubArrayLen(int s, int[] nums)
    {
        int left = 0;
        int right = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;

        while (right < nums.length || sum >= s)
        {
            if (sum < s)
            {
                sum += nums[right++];
            }
            else
            {
                minLen = Math.min(minLen, right - left);
                sum -= nums[left++];
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}


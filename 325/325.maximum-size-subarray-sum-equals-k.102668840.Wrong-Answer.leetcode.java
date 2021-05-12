public class Solution
{
    public int maxSubArrayLen(int[] nums, int k)
    {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);
        int sum = 0;
        int maxLen = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++)
        {
            sum += nums[i];

            if (!map.containsKey(sum))
            {
                map.put(sum, i);
            }
        }

        return maxLen == Integer.MIN_VALUE ? 0 : maxLen;
    }
}

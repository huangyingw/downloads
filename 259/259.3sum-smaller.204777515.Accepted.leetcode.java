public class Solution
{
    public int threeSumSmaller(int[] nums, int target)
    {
        // 先将数组排序
        Arrays.sort(nums);
        int cnt = 0;

        for (int i = 0; i < nums.length - 2; i++)
        {
            int left = i + 1, right = nums.length - 1;

            while (left < right)
            {
                if (nums[i] + nums[left] + nums[right] < target)
                {
                    cnt += right - left;
                    left++;
                }
                else
                {
                    right--;
                }
            }
        }

        return cnt;
    }
}


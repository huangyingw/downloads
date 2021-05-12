public class Solution
{
    public void rotate(int[] nums, int k)
    {
        k %= nums.length;

        for (int i = 0; i < k; i++)
        {
            for (int j = nums.length - 1; j > 0; j--)
            {
                int temp = nums[j];
                nums[j] = nums[j - 1];
                nums[j - 1] = temp;
            }

            System.out.printf("nums --> %s\n", Arrays.toString(nums));
        }
    }
}


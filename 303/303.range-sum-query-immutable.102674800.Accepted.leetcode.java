public class NumArray
{
    private int[] nums;

    public NumArray(int[] nums)
    {
        this.nums = nums;

        for (int i = 1; i < nums.length; i++)
        {
            nums[i] += nums[i - 1];
        }   
    }

    public int sumRange(int i, int j)
    {
        if (i == 0)
        {
            return nums[j];
        }
        
        return nums[j] - nums[i - 1];
    }
}

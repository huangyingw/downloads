  public class Solution
  {
    public void wiggleSort(int[] nums)
    {
      if (nums.length < 2)
      {
        return;
      }

      Arrays.sort(nums);
      int sortedNum[] = Arrays.copyOf(nums, nums.length);
      int j = nums.length - 1;

      for (int i = 1; i < nums.length; i = i + 2)
      {
        nums[i] = sortedNum[j-- ];
      }

      for (int i = 0; i < nums.length; i = i + 2)
      {
        nums[i] = sortedNum[j-- ];
      }
    }
  }


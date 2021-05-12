public class Solution
{
    public int threeSumSmaller(int[] nums, int target)
    {
        Arrays.sort(nums);
        int cnt = 0;

        for (int i = 0; i < nums.length; i++)
        {
            int left = i + 1, right = nums.length - 1;

            while (left < right)
            {
                System.out.printf("i --> %s\n", i) ;
                System.out.printf("left --> %s\n", left) ;
                System.out.printf("right --> %s\n", right) ;

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

